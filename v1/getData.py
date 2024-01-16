import sqlite3


DB = 'sample.sqlite'

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

    def DAU() -> list:

        # ORDER BY count(account_id) DESC
        cursor.execute('''SELECT date, count(account_id)  FROM account_date_session 
                    GROUP BY date 
                    ORDER BY date DESC
                    ;
                    ''')
        conn.commit()

        result = cursor.fetchall()

        return result

    # Sales thing

    def geographic_split_of_revenue() -> list:
        cursor.execute('''select acc.country_code, (sum(pur.iap_price_usd_cents)/100) AS total_by_country from iap_purchase pur
                        join account acc on acc.account_id = pur.account_id
                        group by acc.country_code
                       ''')
        conn.commit()

        result = cursor.fetchall()

        return result

    # This could / and should be resolved with simple right join - > for some reason it was taking super long for sqlite
    # to make querry with right or left joins

    def average_per_country() -> list:

        cursor.execute('''select country_code, count(distinct(account_id)) from account
                            group by country_code
                            order by country_code ASC;
                       ''')
        conn.commit()
        player_count = cursor.fetchall()

        cursor.execute('''select acc.country_code, sum(pur.iap_price_usd_cents) AS total_by_country  from iap_purchase pur
                        join account acc on acc.account_id = pur.account_id
                        group by acc.country_code
                       order by acc.country_code ASC;
                       ''')
        conn.commit()

        purchases_sum = cursor.fetchall()

        return player_count,  purchases_sum

    def geographic_split_of_users() -> None:
        cursor.execute('''select country_code, count(account_id) AS total_by_country  from account
                        group by country_code
                        order by count(account_id) DESC;
                        
                        ''')
        conn.commit()

        result = cursor.fetchall()

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

    def DAU_by_country(country_code) -> list:
        cursor.execute(f"""SELECT s.date, count(s.account_id)  FROM account_date_session s
                join account a on s.account_id = a.account_id
                where a.country_code = '{country_code}'
                    GROUP BY s.date 
                    ORDER BY s.date DESC
                    ;
         
                       """)
        conn.commit()

        result = cursor.fetchall()

        return result

    def DAU_by_country_by_date(country_code) -> list:
        cursor.execute(f"""SELECT s.date, count(s.account_id)  FROM account_date_session s
                join account a on s.account_id = a.account_id
                where a.country_code = '{country_code}'
                    GROUP BY s.date 
                    ORDER BY s.date DESC
                    ;
         
                       """)
        conn.commit()

        result = cursor.fetchall()

        return result

    def country_codes() -> None:
        cursor.execute('''select distinct(country_code) from account;''')
        conn.commit()

        result = cursor.fetchall()

        return result

    def time_sales():

        cursor.execute('''select created_time,sum(iap_price_usd_cents) from iap_purchase
                group by created_time;''')
        conn.commit()

        result = cursor.fetchall()

        return result
    

    def get_platform_data():
        cursor.execute('''SELECT country_code, count(created_platform) from account
                group by country_code''')
        conn.commit()

        all = cursor.fetchall()

        cursor.execute('''SELECT country_code, count(created_platform) from account
                       where created_platform = 'iOS'
                group by country_code
                       
                       ''')
        
        conn.commit()
        iOS = cursor.fetchall()


        cursor.execute('''SELECT country_code, count(created_platform) from account
                       where created_platform = 'Android'
                group by country_code
                       
                       ''')
        
        conn.commit()
        Android = cursor.fetchall()


        return all,iOS,Android


     



