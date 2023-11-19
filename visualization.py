import psycopg2
import matplotlib.pyplot as plt

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

def visualize_bar_chart(labels, values, title, xlabel, ylabel):
    plt.figure(figsize=(10, 15))
    plt.bar(labels, values, width=0.8)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(range(len(labels)), labels, rotation=45) 
    plt.show()

def visualize_pie_chart(labels, sizes, title):
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title(title)
    plt.show()

def visualize_scatter_plot(data, title):
    latitudes = [row[2] for row in data]
    longitudes = [row[3] for row in data]

    plt.scatter(longitudes, latitudes, label='Мільярдери')
    plt.title(title)
    plt.xlabel('Довгота')
    plt.ylabel('Широта')
    plt.legend()
    plt.show()

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
        categories_1 = [row[0] for row in result_1]
        counts_1 = [result_1.count(row) for row in result_1]
        visualize_bar_chart(categories_1, counts_1, 'Назви категорій, власники з США', 'Category', '')

        result_2 = execute_query(cursor, query_2)
        countries = [row[0] for row in result_2]
        counts_2 = [row[1] for row in result_2]
        visualize_pie_chart(countries, counts_2, 'Відсоткове представлення мільярдерів по країнах')

        result_3 = execute_query(cursor, query_3)
        visualize_scatter_plot(result_3, 'Мільярдери та їхні координати')

if __name__ == '__main__':
    main()
