# app.py
import json
import os
import random
import sqlite3
from datetime import datetime, date, timedelta
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)
DB_PATH = os.path.join(os.path.dirname(__file__), 'data', 'hsk3.db')

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/chapters')
def api_chapters():
    level_param = request.args.get('level', 'all')
    conn = get_db()
    cur = conn.cursor()

    sql = "SELECT * FROM chapters"
    params = []
    if level_param != 'all':
        try:
            sql += " WHERE level = ?"
            params.append(int(level_param))
        except ValueError:
            pass

    sql += " ORDER BY level, chapter_num"
    cur.execute(sql, params)
    rows = cur.fetchall()

    chapters = []
    for r in rows:
        chapters.append({
            "id": r["id"],
            "level": r["level"],
            "chapter_num": r["chapter_num"],
            "title_cn": r["title_cn"],
            "title_pinyin": r["title_pinyin"],
            "title_en": r["title_en"],
            "title_th": r["title_th"],
            "topic_en": r["topic_en"],
            "topic_th": r["topic_th"],
            "grammar_en": json.loads(r["grammar_en_json"]) if r["grammar_en_json"] else [],
            "grammar_th": json.loads(r["grammar_th_json"]) if r["grammar_th_json"] else []
        })
    conn.close()
    return jsonify(chapters)

@app.route('/api/session')
def api_session():
    level_param = request.args.get('level', 'all')
    chapter_param = request.args.get('chapters', 'all')
    item_type = request.args.get('type', 'mixed')
    try:
        count = int(request.args.get('count', 18))
    except ValueError:
        count = 18
    only_weak = request.args.get('only_weak', '0') == '1'

    conn = get_db()
    cur = conn.cursor()

    where_clauses = []
    params = []

    if level_param != 'all':
        try:
            where_clauses.append("level = ?")
            params.append(int(level_param))
        except ValueError:
            pass

    if chapter_param != 'all':
        try:
            ch_list = [int(x.strip()) for x in chapter_param.split(',') if x.strip()]
            if ch_list:
                placeholders = ','.join(['?'] * len(ch_list))
                # Support filtering by chapter_num or chapter_id
                where_clauses.append(f"(chapter_num IN ({placeholders}) OR chapter_id IN ({placeholders}))")
                params.extend(ch_list)
                params.extend(ch_list)
        except ValueError:
            pass

    where_sql = f"WHERE {' AND '.join(where_clauses)}" if where_clauses else ""

    words_list = []
    sentences_list = []

    # Query words
    if item_type in ('mixed', 'words'):
        sql = f"""
            SELECT w.*, 
                   COALESCE(r.repetitions, 0) as repetitions,
                   COALESCE(r.last_grade, 0) as last_grade
            FROM words w
            LEFT JOIN review_stats r ON r.item_type = 'word' AND r.item_id = w.id
            {where_sql}
        """
        cur.execute(sql, params)
        for r in cur.fetchall():
            if only_weak and r["last_grade"] > 2:
                continue

            examples = []
            if "examples_json" in r.keys() and r["examples_json"]:
                try:
                    examples = json.loads(r["examples_json"])
                except Exception:
                    examples = []
            if not examples and r["ex_cn"]:
                examples = [{
                    "cn": r["ex_cn"],
                    "py": r["ex_py"],
                    "en": r["ex_en"],
                    "th": r["ex_th"]
                }]

            # Use primary textbook example for consistent initial display
            cur_ex = examples[0] if examples else {
                "cn": r["ex_cn"] or "",
                "py": r["ex_py"] or "",
                "en": r["ex_en"] or "",
                "th": r["ex_th"] or ""
            }

            words_list.append({
                "kind": "word",
                "id": r["id"],
                "level": r["level"],
                "chapter": r["chapter_num"],
                "chapter_id": r["chapter_id"],
                "hanzi": r["hanzi"],
                "pinyin": r["pinyin"],
                "english": r["english"],
                "thai": r["thai"],
                "pos": r["pos"],
                "ex_cn": cur_ex.get("cn", r["ex_cn"]),
                "ex_py": cur_ex.get("py", r["ex_py"]),
                "ex_en": cur_ex.get("en", r["ex_en"]),
                "ex_th": cur_ex.get("th", r["ex_th"]),
                "examples": examples,
                "repetitions": r["repetitions"],
                "last_grade": r["last_grade"]
            })

    # Query sentences
    if item_type in ('mixed', 'sentences'):
        sql = f"""
            SELECT s.*, 
                   COALESCE(r.repetitions, 0) as repetitions,
                   COALESCE(r.last_grade, 0) as last_grade
            FROM sentences s
            LEFT JOIN review_stats r ON r.item_type = 'sentence' AND r.item_id = s.id
            {where_sql}
        """
        cur.execute(sql, params)
        for r in cur.fetchall():
            if only_weak and r["last_grade"] > 2:
                continue
            sentences_list.append({
                "kind": "sentence",
                "id": r["id"],
                "level": r["level"],
                "chapter": r["chapter_num"],
                "chapter_id": r["chapter_id"],
                "context": r["context"],
                "hanzi": r["hanzi"],
                "pinyin": r["pinyin"],
                "english": r["english"],
                "thai": r["thai"],
                "cloze_target": r["cloze_target"],
                "cloze_hint_en": r["cloze_hint_en"],
                "cloze_hint_th": r["cloze_hint_th"],
                "distractors": json.loads(r["distractors_json"]) if ("distractors_json" in r.keys() and r["distractors_json"]) else [],
                "grammar_en": r["grammar_en"],
                "grammar_th": r["grammar_th"],
                "repetitions": r["repetitions"],
                "last_grade": r["last_grade"]
            })

    conn.close()

    random.shuffle(words_list)
    random.shuffle(sentences_list)

    deck = []
    if item_type == 'words':
        deck = words_list[:count]
    elif item_type == 'sentences':
        deck = sentences_list[:count]
    else:
        n_sentences = max(1, count // 3)
        n_words = count - n_sentences
        selected_s = sentences_list[:n_sentences]
        selected_w = words_list[:n_words]
        deck = selected_s + selected_w
        random.shuffle(deck)

    return jsonify({
        "total_available_words": len(words_list),
        "total_available_sentences": len(sentences_list),
        "count": len(deck),
        "items": deck
    })

@app.route('/api/review', methods=['POST'])
def api_review():
    data = request.get_json() or {}
    item_type = data.get('item_type')
    item_id = data.get('item_id')
    grade = int(data.get('grade', 3))
    seconds_spent = int(data.get('seconds_spent', 0))

    if not item_type or not item_id:
        return jsonify({"error": "Missing item_type or item_id"}), 400

    conn = get_db()
    cur = conn.cursor()

    cur.execute("SELECT * FROM review_stats WHERE item_type = ? AND item_id = ?", (item_type, item_id))
    row = cur.fetchone()

    if row:
        reps = row["repetitions"]
        ef = row["ease_factor"]
        interval = row["interval_days"]
    else:
        reps = 0
        ef = 2.5
        interval = 0

    if grade == 1: # Again
        reps = 0
        interval = 0
        ef = max(1.3, ef - 0.2)
    elif grade == 2: # Hard
        reps += 1
        interval = 1 if reps == 1 else max(1, int(interval * 1.2))
        ef = max(1.3, ef - 0.15)
    elif grade == 3: # Good
        if reps == 0:
            interval = 1
        elif reps == 1:
            interval = 3
        else:
            interval = int(interval * ef)
        reps += 1
    elif grade == 4: # Easy
        if reps == 0:
            interval = 2
        elif reps == 1:
            interval = 6
        else:
            interval = int(interval * ef * 1.3)
        reps += 1
        ef = min(3.0, ef + 0.15)

    now = datetime.utcnow()
    next_due = now + timedelta(days=interval)

    cur.execute("""
        INSERT INTO review_stats (item_type, item_id, ease_factor, interval_days, repetitions, last_grade, last_reviewed_at, next_review_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ON CONFLICT(item_type, item_id) DO UPDATE SET
            ease_factor = excluded.ease_factor,
            interval_days = excluded.interval_days,
            repetitions = excluded.repetitions,
            last_grade = excluded.last_grade,
            last_reviewed_at = excluded.last_reviewed_at,
            next_review_at = excluded.next_review_at
    """, (item_type, item_id, ef, interval, reps, grade, now, next_due))

    today_str = date.today().isoformat()
    cur.execute("""
        INSERT INTO daily_streaks (study_date, items_reviewed, minutes_spent)
        VALUES (?, 1, ?)
        ON CONFLICT(study_date) DO UPDATE SET
            items_reviewed = items_reviewed + 1,
            minutes_spent = minutes_spent + ?
    """, (today_str, max(1, seconds_spent // 60), max(1, seconds_spent // 60)))

    conn.commit()
    conn.close()

    return jsonify({
        "success": True,
        "interval_days": interval,
        "repetitions": reps,
        "ease_factor": round(ef, 2)
    })

@app.route('/api/grammar')
def api_grammar():
    level_param = request.args.get('level', 'all')
    chapter_param = request.args.get('chapter', 'all')
    search = request.args.get('q', '').strip()

    conn = get_db()
    cur = conn.cursor()

    sql = "SELECT * FROM grammar_points WHERE 1=1"
    params = []

    if level_param != 'all':
        try:
            sql += " AND level = ?"
            params.append(int(level_param))
        except ValueError:
            pass

    if chapter_param != 'all':
        try:
            sql += " AND chapter_num = ?"
            params.append(int(chapter_param))
        except ValueError:
            pass

    if search:
        sql += " AND (title_cn LIKE ? OR title_th LIKE ? OR structure LIKE ? OR explanation_th LIKE ?)"
        term = f"%{search}%"
        params.extend([term, term, term, term])

    sql += " ORDER BY level, chapter_num, point_num"
    cur.execute(sql, params)

    grammar_points = []
    for r in cur.fetchall():
        grammar_points.append({
            "id": r["id"],
            "level": r["level"],
            "chapter_num": r["chapter_num"],
            "point_num": r["point_num"],
            "title_cn": r["title_cn"],
            "title_th": r["title_th"],
            "structure": r["structure"],
            "explanation_th": r["explanation_th"],
            "examples": json.loads(r["examples_json"]) if r["examples_json"] else []
        })

    conn.close()
    return jsonify(grammar_points)

@app.route('/api/stats')
def api_stats():
    conn = get_db()
    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) FROM words")
    total_words = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM sentences")
    total_sentences = cur.fetchone()[0]

    # Count by level
    cur.execute("SELECT level, COUNT(*) FROM words GROUP BY level")
    words_by_level = {f"level_{r[0]}": r[1] for r in cur.fetchall()}

    cur.execute("SELECT COUNT(*) FROM review_stats WHERE item_type = 'word'")
    reviewed_words = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM review_stats WHERE item_type = 'word' AND repetitions >= 3")
    mastered_words = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM review_stats WHERE item_type = 'word' AND last_grade = 1")
    need_review_words = cur.fetchone()[0]

    cur.execute("SELECT study_date, items_reviewed FROM daily_streaks ORDER BY study_date DESC LIMIT 30")
    streaks_rows = cur.fetchall()

    today = date.today()
    streak_count = 0
    checked_date = today

    dates_studied = {r["study_date"] for r in streaks_rows}
    if today.isoformat() in dates_studied:
        streak_count += 1
        checked_date = today - timedelta(days=1)
    else:
        yesterday = today - timedelta(days=1)
        if yesterday.isoformat() in dates_studied:
            streak_count += 1
            checked_date = yesterday - timedelta(days=1)

    while checked_date.isoformat() in dates_studied:
        streak_count += 1
        checked_date -= timedelta(days=1)

    today_items = 0
    for r in streaks_rows:
        if r["study_date"] == today.isoformat():
            today_items = r["items_reviewed"]
            break

    conn.close()

    return jsonify({
        "total_words": total_words,
        "total_sentences": total_sentences,
        "words_by_level": words_by_level,
        "reviewed_words": reviewed_words,
        "mastered_words": mastered_words,
        "need_review_words": need_review_words,
        "current_streak": streak_count,
        "today_reviewed": today_items,
        "daily_goal": 20
    })

@app.route('/api/dictionary')
def api_dictionary():
    level_param = request.args.get('level', 'all')
    chapter = request.args.get('chapter', 'all')
    search = request.args.get('q', '').strip()

    conn = get_db()
    cur = conn.cursor()

    sql = """
        SELECT w.*, 
               COALESCE(r.repetitions, 0) as repetitions,
               COALESCE(r.last_grade, 0) as last_grade
            FROM words w
            LEFT JOIN review_stats r ON r.item_type = 'word' AND r.item_id = w.id
            WHERE 1=1
    """
    params = []

    if level_param != 'all':
        try:
            sql += " AND w.level = ?"
            params.append(int(level_param))
        except ValueError:
            pass

    if chapter != 'all':
        try:
            sql += " AND (w.chapter_num = ? OR w.chapter_id = ?)"
            c_int = int(chapter)
            params.extend([c_int, c_int])
        except ValueError:
            pass

    if search:
        sql += " AND (w.hanzi LIKE ? OR w.pinyin LIKE ? OR w.english LIKE ? OR w.thai LIKE ?)"
        term = f"%{search}%"
        params.extend([term, term, term, term])

    sql += " ORDER BY w.level, w.chapter_num, w.id"
    cur.execute(sql, params)

    words = []
    for r in cur.fetchall():
        examples = []
        if "examples_json" in r.keys() and r["examples_json"]:
            try:
                examples = json.loads(r["examples_json"])
            except Exception:
                examples = []
        if not examples and r["ex_cn"]:
            examples = [{
                "cn": r["ex_cn"],
                "py": r["ex_py"],
                "en": r["ex_en"],
                "th": r["ex_th"]
            }]

        words.append({
            "id": r["id"],
            "level": r["level"],
            "chapter": r["chapter_num"],
            "chapter_id": r["chapter_id"],
            "hanzi": r["hanzi"],
            "pinyin": r["pinyin"],
            "english": r["english"],
            "thai": r["thai"],
            "pos": r["pos"],
            "ex_cn": r["ex_cn"],
            "ex_py": r["ex_py"],
            "ex_en": r["ex_en"],
            "ex_th": r["ex_th"],
            "examples": examples,
            "repetitions": r["repetitions"],
            "last_grade": r["last_grade"]
        })

    conn.close()
    return jsonify(words)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
