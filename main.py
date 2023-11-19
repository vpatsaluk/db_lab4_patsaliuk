import psycopg2
from tabulate import tabulate

db_params = {
    'host': 'localhost',
    'database': 'db_lab3',
    'user': 'postgres',
    'password': '1805',
    'port': '5432'
}

query_1 = '''
    SELECT DISTINCT o.category_org
    FROM Billionaire b
    JOIN organization o ON b.name_org = o.name_org
    JOIN country c ON b.name_country = c.name_country
    WHERE c.name_country = 'United States';
'''

query_2 = '''
    SELECT c.name_country, COUNT(*) AS billionaire_count
    FROM Billionaire b
    JOIN Country c ON b.name_country = c.name_country
    GROUP BY c.name_country;
'''

query_3 = '''
    SELECT b.firstname, b.lastname, c.latitude_country, c.longtitude_country
    FROM Billionaire b
    JOIN Country c ON b.name_country = c.name_country;
'''

def execute_query(cursor, query):
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def print_query_results(query, result, cursor):
    print(f"\nQuery: {query}\n")
    headers = [desc[0] for desc in cursor.description]
    print(tabulate(result, headers, tablefmt="pretty"))

def main():
    connection = psycopg2.connect(
        user=db_params['user'],
        password=db_params['password'],
        dbname=db_params['database'],
        host=db_params['host'],
        port=db_params['port']
    )

    with connection.cursor() as cursor:
        result_1 = execute_query(cursor, query_1)
        print_query_results(query_1, result_1, cursor)

        result_2 = execute_query(cursor, query_2)
        print_query_results(query_2, result_2, cursor)

        result_3 = execute_query(cursor, query_3)
        print_query_results(query_3, result_3, cursor)

if __name__ == '__main__':
    main()