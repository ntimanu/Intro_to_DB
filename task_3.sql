USE alx_book_store;

SELECT table_name 
FROM information_schema.tables 
WHERE table_schema = DATABASE();
