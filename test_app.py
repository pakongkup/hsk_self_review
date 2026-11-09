# test_app.py
import sys
sys.stdout.reconfigure(encoding='utf-8')

from app import app

client = app.test_client()

print("--- Testing GET / ---")
res = client.get('/')
assert res.status_code == 200, f"Expected 200, got {res.status_code}"
assert b"HSK Review" in res.data
print("✓ GET / passed!")

print("--- Testing GET /api/chapters (Multi-Level) ---")
res = client.get('/api/chapters')
assert res.status_code == 200
chapters = res.json
assert len(chapters) == 48, f"Expected 48 chapters total, got {len(chapters)}"
print(f"✓ GET /api/chapters all passed! ({len(chapters)} chapters)")

res_l1 = client.get('/api/chapters?level=1')
assert len(res_l1.json) == 15
print(f"✓ GET /api/chapters?level=1 passed! ({len(res_l1.json)} chapters)")

res_l2 = client.get('/api/chapters?level=2')
assert len(res_l2.json) == 15
print(f"✓ GET /api/chapters?level=2 passed! ({len(res_l2.json)} chapters)")

res_l3 = client.get('/api/chapters?level=3')
assert len(res_l3.json) == 18
print(f"✓ GET /api/chapters?level=3 passed! ({len(res_l3.json)} chapters)")

print("--- Testing GET /api/session (Level 2) ---")
res = client.get('/api/session?level=2&count=10&type=mixed')
assert res.status_code == 200
session_data = res.json
assert "items" in session_data
assert len(session_data["items"]) == 10
for item in session_data["items"]:
    assert item["level"] == 2
print(f"✓ GET /api/session?level=2 passed! (10 items verified level 2)")

print("--- Testing GET /api/grammar (Grammar Summary Menu) ---")
res = client.get('/api/grammar')
assert res.status_code == 200
grammar_all = res.json
assert len(grammar_all) >= 60, f"Expected >= 60 grammar points, got {len(grammar_all)}"
print(f"✓ GET /api/grammar passed! ({len(grammar_all)} grammar points across levels)")

res_g2 = client.get('/api/grammar?level=2')
assert len(res_g2.json) > 0
print(f"✓ GET /api/grammar?level=2 passed! ({len(res_g2.json)} grammar points)")

res_g_search = client.get('/api/grammar?q=是')
assert len(res_g_search.json) > 0
print(f"✓ GET /api/grammar search for '是' passed! ({len(res_g_search.json)} results)")

print("--- Testing POST /api/review ---")
res = client.post('/api/review', json={
    "item_type": "word",
    "item_id": 1,
    "grade": 3,
    "seconds_spent": 8
})
assert res.status_code == 200
review_res = res.json
assert review_res["success"] is True
print(f"✓ POST /api/review passed! (Updated interval: {review_res['interval_days']} days)")

print("--- Testing GET /api/stats ---")
res = client.get('/api/stats')
assert res.status_code == 200
stats = res.json
assert stats["total_words"] >= 500
print(f"✓ GET /api/stats passed! (Total words: {stats['total_words']}, Sentences: {stats['total_sentences']})")

print("--- Testing GET /api/dictionary (Level 1 Thai Search) ---")
res = client.get('/api/dictionary?level=1&q=ขอบคุณ')
assert res.status_code == 200
dict_res = res.json
assert len(dict_res) >= 1
assert dict_res[0]["hanzi"] == "谢谢"
print(f"✓ GET /api/dictionary search for 'ขอบคุณ' passed! Found: {dict_res[0]['hanzi']} ({dict_res[0]['thai']})")

print("\n🎉 ALL 8 TEST SUITES PASSED CLEANLY! The application is rock solid.")
