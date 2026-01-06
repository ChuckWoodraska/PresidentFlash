import sqlite3
import os

def init_db():
    # Ensure the directory exists
    os.makedirs("data", exist_ok=True)
    
    conn = sqlite3.connect("data/presidents.db")
    cursor = conn.cursor()

    # Create tables
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS presidents (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        number INTEGER,
        name TEXT,
        years TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS legislation (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        president_id INTEGER,
        name TEXT,
        FOREIGN KEY(president_id) REFERENCES presidents(id)
    )
    """)

    # Data
    presidents_data = [
        (1, "George Washington", "1789-1797", ["Judiciary Act of 1789", "Naturalization Act of 1790", "Residence Act of 1790", "Fugitive Slave Act of 1793"]),
        (2, "John Adams", "1797-1801", ["Alien and Sedition Acts", "Naturalization Act of 1798"]),
        (3, "Thomas Jefferson", "1801-1809", ["Embargo Act of 1807", "Act Prohibiting Importation of Slaves", "Military Peace Establishment Act"]),
        (4, "James Madison", "1809-1817", ["Macon's Bill Number 2", "Charter of the Second Bank of the United States"]),
        (5, "James Monroe", "1817-1825", ["Missouri Compromise", "Tenure of Office Act of 1820"]),
        (6, "John Quincy Adams", "1825-1829", ["Tariff of 1828 (Tariff of Abominations)"]),
        (7, "Andrew Jackson", "1829-1837", ["Indian Removal Act", "Force Bill", "Deposit and Distribution Act"]),
        (8, "Martin Van Buren", "1837-1841", ["Independent Treasury Act"]),
        (9, "William Henry Harrison", "1841", []),
        (10, "John Tyler", "1841-1845", ["Log Cabin Bill", "Bankruptcy Act of 1841"]),
        (11, "James K. Polk", "1845-1849", ["Walker Tariff", "Independent Treasury Act of 1846"]),
        (12, "Zachary Taylor", "1849-1850", []),
        (13, "Millard Fillmore", "1850-1853", ["Compromise of 1850", "Fugitive Slave Act of 1850"]),
        (14, "Franklin Pierce", "1853-1857", ["Kansas-Nebraska Act"]),
        (15, "James Buchanan", "1857-1861", ["Admission of Kansas"]),
        (16, "Abraham Lincoln", "1861-1865", ["Homestead Act", "Morrill Land-Grant Acts", "Pacific Railroad Acts", "National Banking Acts", "Revenue Act of 1861"]),
        (17, "Andrew Johnson", "1865-1869", ["Southern Homestead Act of 1866", "Tenure of Office Act (1867)"]),
        (18, "Ulysses S. Grant", "1869-1877", ["Enforcement Acts", "Civil Rights Act of 1875", "Public Credit Act of 1869", "Coinage Act of 1873"]),
        (19, "Rutherford B. Hayes", "1877-1881", ["Bland-Allison Act"]),
        (20, "James A. Garfield", "1881", []),
        (21, "Chester A. Arthur", "1881-1885", ["Pendleton Civil Service Reform Act", "Chinese Exclusion Act"]),
        (22, "Grover Cleveland", "1885-1889", ["Interstate Commerce Act of 1887", "Dawes Act"]),
        (23, "Benjamin Harrison", "1889-1893", ["Sherman Antitrust Act", "McKinley Tariff", "Sherman Silver Purchase Act"]),
        (24, "Grover Cleveland", "1893-1897", ["Wilson-Gorman Tariff Act"]),
        (25, "William McKinley", "1897-1901", ["Dingley Act", "Gold Standard Act"]),
        (26, "Theodore Roosevelt", "1901-1909", ["Pure Food and Drug Act", "Meat Inspection Act", "Hepburn Act", "Antiquities Act"]),
        (27, "William Howard Taft", "1909-1913", ["Payne-Aldrich Tariff Act", "Mann-Elkins Act"]),
        (28, "Woodrow Wilson", "1913-1921", ["Federal Reserve Act", "Clayton Antitrust Act", "Federal Trade Commission Act", "Espionage Act of 1917"]),
        (29, "Warren G. Harding", "1921-1923", ["Budget and Accounting Act", "Fordney-McCumber Tariff"]),
        (30, "Calvin Coolidge", "1923-1929", ["Immigration Act of 1924", "Revenue Acts of 1924 and 1926"]),
        (31, "Herbert Hoover", "1929-1933", ["Smoot-Hawley Tariff Act", "Reconstruction Finance Corporation Act"]),
        (32, "Franklin D. Roosevelt", "1933-1945", ["Social Security Act", "Glass-Steagall Act", "National Labor Relations Act", "Lend-Lease Act", "Fair Labor Standards Act"]),
        (33, "Harry S. Truman", "1945-1953", ["National Security Act of 1947", "Marshall Plan", "Housing Act of 1949"]),
        (34, "Dwight D. Eisenhower", "1953-1961", ["Federal Aid Highway Act of 1956", "Civil Rights Act of 1957", "National Defense Education Act"]),
        (35, "John F. Kennedy", "1961-1963", ["Peace Corps Act", "Clean Air Act (1963)", "Equal Pay Act of 1963"]),
        (36, "Lyndon B. Johnson", "1963-1969", ["Civil Rights Act of 1964", "Voting Rights Act of 1965", "Social Security Amendments of 1965 (Medicare/Medicaid)", "Elementary and Secondary Education Act"]),
        (37, "Richard Nixon", "1969-1974", ["National Environmental Policy Act", "Clean Air Act of 1970", "Endangered Species Act"]),
        (38, "Gerald Ford", "1974-1977", ["Privacy Act of 1974", "Education for All Handicapped Children Act"]),
        (39, "Jimmy Carter", "1977-1981", ["Department of Energy Organization Act", "Airline Deregulation Act", "Staggers Rail Act"]),
        (40, "Ronald Reagan", "1981-1989", ["Economic Recovery Tax Act of 1981", "Tax Reform Act of 1986", "Immigration Reform and Control Act of 1986"]),
        (41, "George H. W. Bush", "1989-1993", ["Americans with Disabilities Act", "Clean Air Act Amendments of 1990", "Immigration Act of 1990"]),
        (42, "Bill Clinton", "1993-2001", ["Violent Crime Control and Law Enforcement Act", "Personal Responsibility and Work Opportunity Reconciliation Act", "North American Free Trade Agreement Implementation Act"]),
        (43, "George W. Bush", "2001-2009", ["No Child Left Behind Act", "USA PATRIOT Act", "Emergency Economic Stabilization Act of 2008"]),
        (44, "Barack Obama", "2009-2017", ["Affordable Care Act", "Dodd-Frank Wall Street Reform and Consumer Protection Act", "American Recovery and Reinvestment Act"]),
        (45, "Donald Trump", "2017-2021", ["Tax Cuts and Jobs Act of 2017", "First Step Act", "CARES Act"]),
        (46, "Joe Biden", "2021-Present", ["American Rescue Plan Act", "Infrastructure Investment and Jobs Act", "Inflation Reduction Act"])
    ]

    for number, name, years, acts in presidents_data:
        cursor.execute("INSERT INTO presidents (number, name, years) VALUES (?, ?, ?)", (number, name, years))
        president_id = cursor.lastrowid
        for act in acts:
            cursor.execute("INSERT INTO legislation (president_id, name) VALUES (?, ?)", (president_id, act))

    conn.commit()
    conn.close()
    print("Database initialized successfully.")

if __name__ == "__main__":
    init_db()
