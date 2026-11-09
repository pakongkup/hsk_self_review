# test_app.py
import sys
sys.stdout.reconfigure(encoding='utf-8')

from app import app

client = app.test_client()

print("--- Testing GET / ---")
res = client.get('/')
assert res.status_code == 200, f"Expected 200, got {res.status_code}"
assert b"HSK 3 Review" in res.data
print("✓ GET / passed!")

print("--- Testing GET /api/chapters ---")
res = client.get('/api/chapters')
assert res.status_code == 200
chapters = res.json
assert len(chapters) == 18, f"Expected 18 chapters, got {len(chapters)}"
assert chapters[0]["title_cn"] == "我们去机场接你们"
print(f"✓ GET /api/chapters passed! ({len(chapters)} chapters)")

print("--- Testing GET /api/session ---")
res = client.get('/api/session?chapters=1,2,3&count=10&type=mixed')
assert res.status_code == 200
session_data = res.json
assert "items" in session_data
assert len(session_data["items"]) == 10
kinds = set(item["kind"] for item in session_data["items"])
print(f"✓ GET /api/session passed! (Returned {len(session_data['items'])} items, kinds: {kinds})")

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
print(f"✓ GET /api/stats passed! (Total words: {stats['total_words']}, Streaks: {stats['current_streak']})")

print("--- Testing GET /api/dictionary ---")
res = client.get('/api/dictionary?q=机场')
assert res.status_code == 200
dict_res = res.json
print(f"✓ GET /api/dictionary search for '机场' passed! Found {len(dict_res)} results.")

print("\n🎉 ALL TESTS PASSED SUCCESSFULLY! The application backend is solid.")
