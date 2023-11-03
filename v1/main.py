import sqlite3


DB = 'v1/sample.sqlite'

with sqlite3.connect(DB) as conn:

    cursor = conn.cursor()

    # The most active users
    def reverse_DAU() -> None:

        cursor.execute('''SELECT account_id, count(date)  FROM account_date_session 
                    GROUP BY account_id 
                    ORDER BY count(date) ASC
                    LIMIT 10;
                    ''')
        conn.commit()

        result = cursor.fetchall()
        print(result)

    # Highest peak of users

    def DAU() -> None:

        cursor.execute('''SELECT date, count(account_id)  FROM account_date_session 
                    GROUP BY date 
                    ORDER BY count(account_id) DESC
                    LIMIT 10;
                    ''')
        conn.commit()

        result = cursor.fetchall()
        print(result)

    # Sales thing

    def geographic_split_of_revenue() -> None:
        cursor.execute('''select acc.country_code, sum(pur.iap_price_usd_cents) AS total_by_country  from iap_purchase pur
                        join account acc on acc.account_id = pur.account_id
                        group by acc.country_code
                       ''')
        conn.commit()

        result = cursor.fetchall()
        print(result)

    def geographic_split_of_users() -> None:
        cursor.execute('''select acc.country_code, count(acc.account_id) AS total_by_country  from iap_purchase pur
                        join account acc on acc.account_id = pur.account_id
                        group by acc.country_code;
                       ''')
        conn.commit()

        result = cursor.fetchall()
        print(result)

    def geographic_split_of_time() -> None:

        cursor.execute('''select acc.country_code, sum(pur.session_duration_sec) AS total_by_country  from account_date_session pur
                        join account acc on acc.account_id = pur.account_id
                        group by acc.country_code
						order by sum(pur.session_duration_sec) DESC
						;
						
                       ''')
        conn.commit()

        result = cursor.fetchall()
        print(result)

geographic_split_of_time()
