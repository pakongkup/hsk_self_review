# build_master_database.py
import os
import sys
import json
import sqlite3

sys.stdout.reconfigure(encoding='utf-8')

from build_full_hsk_database import chapters_data
from data_hsk1 import hsk1_words, hsk1_sentences, hsk1_grammar
from data_hsk2 import hsk2_words, hsk2_sentences, hsk2_grammar
from create_hsk3_full_database import words_data as hsk3_words, sentences_data as hsk3_sentences
from data_hsk3_grammar import hsk3_grammar

DB_PATH = os.path.join(os.path.dirname(__file__), 'data', 'hsk3.db')
JSON_PATH = os.path.join(os.path.dirname(__file__), 'data', 'hsk3_database.json')

def main():
    print("==================================================")
    print("🚀 Building Multi-Level HSK Master Database")
    print("==================================================")

    # 1. Prepare Chapters map
    # Maps (level, chapter_num) -> chapter_id
    ch_map = {}
    for ch in chapters_data:
        ch_map[(ch["level"], ch["chapter_num"])] = ch["id"]

    # 2. Prepare Words
    all_words = []
    word_id = 1

    # HSK 1 Words
    for w in hsk1_words:
        lvl = 1
        ch_num = w["chapter_num"]
        ch_id = ch_map.get((lvl, ch_num), 100 + ch_num)
        all_words.append({
            "id": word_id,
            "level": lvl,
            "chapter_id": ch_id,
            "chapter_num": ch_num,
            "hanzi": w["hanzi"],
            "pinyin": w["pinyin"],
            "english": w["english"],
            "thai": w["thai"],
            "pos": w["pos"],
            "ex_cn": w.get("ex_cn", ""),
            "ex_py": w.get("ex_py", ""),
            "ex_en": w.get("ex_en", ""),
            "ex_th": w.get("ex_th", "")
        })
        word_id += 1

    # HSK 2 Words
    for w in hsk2_words:
        lvl = 2
        ch_num = w["chapter_num"]
        ch_id = ch_map.get((lvl, ch_num), 200 + ch_num)
        all_words.append({
            "id": word_id,
            "level": lvl,
            "chapter_id": ch_id,
            "chapter_num": ch_num,
            "hanzi": w["hanzi"],
            "pinyin": w["pinyin"],
            "english": w["english"],
            "thai": w["thai"],
            "pos": w["pos"],
            "ex_cn": w.get("ex_cn", ""),
            "ex_py": w.get("ex_py", ""),
            "ex_en": w.get("ex_en", ""),
            "ex_th": w.get("ex_th", "")
        })
        word_id += 1

    # HSK 3 Words
    for w in hsk3_words:
        lvl = 3
        ch_num = w["chapter"]
        ch_id = ch_map.get((lvl, ch_num), 300 + ch_num)
        all_words.append({
            "id": word_id,
            "level": lvl,
            "chapter_id": ch_id,
            "chapter_num": ch_num,
            "hanzi": w["hanzi"],
            "pinyin": w["pinyin"],
            "english": w["english"],
            "thai": w.get("thai", ""),
            "pos": w["pos"],
            "ex_cn": w.get("ex_cn", ""),
            "ex_py": w.get("ex_py", ""),
            "ex_en": w.get("ex_en", ""),
            "ex_th": w.get("ex_th", "")
        })
        word_id += 1

    # 3. Prepare Sentences
    all_sentences = []
    sent_id = 1

    # HSK 1 Sentences
    for s in hsk1_sentences:
        lvl = 1
        ch_num = s["chapter_num"]
        ch_id = ch_map.get((lvl, ch_num), 100 + ch_num)
        all_sentences.append({
            "id": sent_id,
            "level": lvl,
            "chapter_id": ch_id,
            "chapter_num": ch_num,
            "context": s.get("context", ""),
            "hanzi": s["hanzi"],
            "pinyin": s["pinyin"],
            "english": s["english"],
            "thai": s["thai"],
            "cloze_target": s["cloze_target"],
            "cloze_hint_en": s["cloze_hint_en"],
            "cloze_hint_th": s["cloze_hint_th"],
            "grammar_en": s["grammar_en"],
            "grammar_th": s["grammar_th"]
        })
        sent_id += 1

    # HSK 2 Sentences
    for s in hsk2_sentences:
        lvl = 2
        ch_num = s["chapter_num"]
        ch_id = ch_map.get((lvl, ch_num), 200 + ch_num)
        all_sentences.append({
            "id": sent_id,
            "level": lvl,
            "chapter_id": ch_id,
            "chapter_num": ch_num,
            "context": s.get("context", ""),
            "hanzi": s["hanzi"],
            "pinyin": s["pinyin"],
            "english": s["english"],
            "thai": s["thai"],
            "cloze_target": s["cloze_target"],
            "cloze_hint_en": s["cloze_hint_en"],
            "cloze_hint_th": s["cloze_hint_th"],
            "grammar_en": s["grammar_en"],
            "grammar_th": s["grammar_th"]
        })
        sent_id += 1

    # HSK 3 Sentences
    for s in hsk3_sentences:
        lvl = 3
        ch_num = s["chapter"]
        ch_id = ch_map.get((lvl, ch_num), 300 + ch_num)
        all_sentences.append({
            "id": sent_id,
            "level": lvl,
            "chapter_id": ch_id,
            "chapter_num": ch_num,
            "context": s.get("context", ""),
            "hanzi": s["hanzi"],
            "pinyin": s["pinyin"],
            "english": s["english"],
            "thai": s.get("thai", ""),
            "cloze_target": s["cloze_target"],
            "cloze_hint_en": s.get("cloze_hint_en") or s.get("cloze_hint", ""),
            "cloze_hint_th": s.get("cloze_hint_th") or s.get("thai", ""),
            "grammar_en": s.get("grammar_en") or s.get("grammar_point", ""),
            "grammar_th": s.get("grammar_th", "")
        })
        sent_id += 1

    # 4. Prepare Grammar Points
    all_grammar_points = []
    gp_id = 1

    for gp in hsk1_grammar:
        all_grammar_points.append({
            "id": gp_id,
            "level": 1,
            "chapter_num": gp["chapter_num"],
            "point_num": gp["point_num"],
            "title_cn": gp["title_cn"],
            "title_th": gp["title_th"],
            "structure": gp["structure"],
            "explanation_th": gp["explanation_th"],
            "examples": gp["examples"]
        })
        gp_id += 1

    for gp in hsk2_grammar:
        all_grammar_points.append({
            "id": gp_id,
            "level": 2,
            "chapter_num": gp["chapter_num"],
            "point_num": gp["point_num"],
            "title_cn": gp["title_cn"],
            "title_th": gp["title_th"],
            "structure": gp["structure"],
            "explanation_th": gp["explanation_th"],
            "examples": gp["examples"]
        })
        gp_id += 1

    for gp in hsk3_grammar:
        all_grammar_points.append({
            "id": gp_id,
            "level": 3,
            "chapter_num": gp["chapter_num"],
            "point_num": gp["point_num"],
            "title_cn": gp["title_cn"],
            "title_th": gp["title_th"],
            "structure": gp["structure"],
            "explanation_th": gp["explanation_th"],
            "examples": gp["examples"]
        })
        gp_id += 1

    print(f"Total Chapters:       {len(chapters_data)}")
    print(f"Total Words:          {len(all_words)}")
    print(f"Total Sentences:      {len(all_sentences)}")
    print(f"Total Grammar Points: {len(all_grammar_points)}")

    # 5. Populate SQLite Database
    if os.path.exists(DB_PATH):
        # We can back up or keep review_stats and daily_streaks
        conn_old = sqlite3.connect(DB_PATH)
        cur_old = conn_old.cursor()
        try:
            cur_old.execute("SELECT * FROM review_stats")
            old_review_stats = cur_old.fetchall()
        except:
            old_review_stats = []
        try:
            cur_old.execute("SELECT * FROM daily_streaks")
            old_daily_streaks = cur_old.fetchall()
        except:
            old_daily_streaks = []
        conn_old.close()
    else:
        old_review_stats = []
        old_daily_streaks = []

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("DROP TABLE IF EXISTS chapters")
    cur.execute("DROP TABLE IF EXISTS words")
    cur.execute("DROP TABLE IF EXISTS sentences")
    cur.execute("DROP TABLE IF EXISTS grammar_points")
    cur.execute("DROP TABLE IF EXISTS review_stats")
    cur.execute("DROP TABLE IF EXISTS daily_streaks")

    cur.execute("""
        CREATE TABLE chapters (
            id INTEGER PRIMARY KEY,
            level INTEGER NOT NULL,
            chapter_num INTEGER NOT NULL,
            title_cn TEXT NOT NULL,
            title_pinyin TEXT NOT NULL,
            title_en TEXT NOT NULL,
            title_th TEXT NOT NULL,
            topic_en TEXT,
            topic_th TEXT,
            grammar_en_json TEXT,
            grammar_th_json TEXT
        )
    """)

    cur.execute("""
        CREATE TABLE words (
            id INTEGER PRIMARY KEY,
            level INTEGER NOT NULL,
            chapter_id INTEGER NOT NULL,
            chapter_num INTEGER NOT NULL,
            hanzi TEXT NOT NULL,
            pinyin TEXT NOT NULL,
            english TEXT NOT NULL,
            thai TEXT NOT NULL,
            pos TEXT,
            ex_cn TEXT,
            ex_py TEXT,
            ex_en TEXT,
            ex_th TEXT,
            FOREIGN KEY (chapter_id) REFERENCES chapters(id)
        )
    """)

    cur.execute("""
        CREATE TABLE sentences (
            id INTEGER PRIMARY KEY,
            level INTEGER NOT NULL,
            chapter_id INTEGER NOT NULL,
            chapter_num INTEGER NOT NULL,
            context TEXT,
            hanzi TEXT NOT NULL,
            pinyin TEXT NOT NULL,
            english TEXT NOT NULL,
            thai TEXT NOT NULL,
            cloze_target TEXT NOT NULL,
            cloze_hint_en TEXT,
            cloze_hint_th TEXT,
            grammar_en TEXT,
            grammar_th TEXT,
            FOREIGN KEY (chapter_id) REFERENCES chapters(id)
        )
    """)

    cur.execute("""
        CREATE TABLE grammar_points (
            id INTEGER PRIMARY KEY,
            level INTEGER NOT NULL,
            chapter_num INTEGER NOT NULL,
            point_num INTEGER NOT NULL,
            title_cn TEXT NOT NULL,
            title_th TEXT NOT NULL,
            structure TEXT,
            explanation_th TEXT NOT NULL,
            examples_json TEXT NOT NULL
        )
    """)

    cur.execute("""
        CREATE TABLE review_stats (
            item_type TEXT NOT NULL,
            item_id INTEGER NOT NULL,
            ease_factor REAL DEFAULT 2.5,
            interval_days INTEGER DEFAULT 0,
            repetitions INTEGER DEFAULT 0,
            last_grade INTEGER DEFAULT 0,
            last_reviewed_at TIMESTAMP,
            next_review_at TIMESTAMP,
            PRIMARY KEY (item_type, item_id)
        )
    """)

    cur.execute("""
        CREATE TABLE daily_streaks (
            study_date TEXT PRIMARY KEY,
            items_reviewed INTEGER DEFAULT 0,
            minutes_spent INTEGER DEFAULT 0
        )
    """)

    # Insert Chapters
    for ch in chapters_data:
        cur.execute("""
            INSERT INTO chapters (id, level, chapter_num, title_cn, title_pinyin, title_en, title_th, topic_en, topic_th, grammar_en_json, grammar_th_json)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            ch["id"],
            ch["level"],
            ch["chapter_num"],
            ch["title_cn"],
            ch["title_pinyin"],
            ch["title_en"],
            ch["title_th"],
            ch.get("topic_en", ""),
            ch.get("topic_th", ""),
            json.dumps(ch.get("grammar_en", []), ensure_ascii=False),
            json.dumps(ch.get("grammar_th", []), ensure_ascii=False)
        ))

    # Insert Words
    for w in all_words:
        cur.execute("""
            INSERT INTO words (id, level, chapter_id, chapter_num, hanzi, pinyin, english, thai, pos, ex_cn, ex_py, ex_en, ex_th)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            w["id"], w["level"], w["chapter_id"], w["chapter_num"],
            w["hanzi"], w["pinyin"], w["english"], w["thai"], w["pos"],
            w["ex_cn"], w["ex_py"], w["ex_en"], w["ex_th"]
        ))

    # Insert Sentences
    for s in all_sentences:
        cur.execute("""
            INSERT INTO sentences (id, level, chapter_id, chapter_num, context, hanzi, pinyin, english, thai, cloze_target, cloze_hint_en, cloze_hint_th, grammar_en, grammar_th)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            s["id"], s["level"], s["chapter_id"], s["chapter_num"],
            s["context"], s["hanzi"], s["pinyin"], s["english"], s["thai"],
            s["cloze_target"], s["cloze_hint_en"], s["cloze_hint_th"],
            s["grammar_en"], s["grammar_th"]
        ))

    # Insert Grammar Points
    for gp in all_grammar_points:
        cur.execute("""
            INSERT INTO grammar_points (id, level, chapter_num, point_num, title_cn, title_th, structure, explanation_th, examples_json)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            gp["id"], gp["level"], gp["chapter_num"], gp["point_num"],
            gp["title_cn"], gp["title_th"], gp["structure"], gp["explanation_th"],
            json.dumps(gp["examples"], ensure_ascii=False)
        ))

    conn.commit()
    conn.close()

    # 6. Save Database JSON
    full_db = {
        "chapters": chapters_data,
        "words": all_words,
        "sentences": all_sentences,
        "grammar_points": all_grammar_points
    }
    with open(JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(full_db, f, ensure_ascii=False, indent=2)

    print("Master database successfully created at:")
    print(f"  ✓ SQLite: {DB_PATH}")
    print(f"  ✓ JSON:   {JSON_PATH}")

if __name__ == "__main__":
    main()
