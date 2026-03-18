from database import initialize_database, insert_raw_articles

initialize_database()

insert_raw_articles(
    title="Test Article1",
    link="https://example.com/test1",
    source="Test Source",
    published_date="2026-03-03",
    content="This is a test content for F1 article."
)

print("Insert test completed.")