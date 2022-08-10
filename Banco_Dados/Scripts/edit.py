schema_order_reviews = """
    CREATE TABLE order_reviews(
    review_id                  object
order_id                   object
review_score                int64
review_comment_title       object
review_comment_message     object
review_creation_date       object
review_answer_timestamp    object)

"""
schema_orders = """
    CREATE TABLE orders(
    customer_id             TEXT,
    customer_unique_id      TEXT,
    customer_zip_cod_prefix INTEGER,
    customer_city           TEXT,
    customer_state          TEXT)

"""
schema_products = """
    CREATE TABLE products(
    customer_id             TEXT,
    customer_unique_id      TEXT,
    customer_zip_cod_prefix INTEGER,
    customer_city           TEXT,
    customer_state          TEXT)

"""
schema_sellers = """
    CREATE TABLE sellers(
    customer_id             TEXT,
    customer_unique_id      TEXT,
    customer_zip_cod_prefix INTEGER,
    customer_city           TEXT,
    customer_state          TEXT)

"""
schema_product_category_name = """
    CREATE TABLE product_category_name(
    customer_id             TEXT,
    customer_unique_id      TEXT,
    customer_zip_cod_prefix INTEGER,
    customer_city           TEXT,
    customer_state          TEXT)

"""
