import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    global city
    city = input("Enter name of the city to analyze (chicago, new york city, washington): ").lower()  
    while city not in CITY_DATA:
            print("City is not on the list.")
            city = input("Enter name of the city to analyze (chicago, new york city, washington): ").lower()      
   
    # TO DO: get user input for month (all, january, february, ... , june)
    month_list = ('all', 'january', 'february','march','april','may','june')
    month = input("Enter name of the month from january to june to filter by, or 'all' to apply no month filter: ").lower()
    
    while month not in month_list:
            print("Month is not on the list.")
            month = input("Enter name of the month from january to june to filter by, or 'all' to apply no month filter: ").lower() 
            
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_list = ('all','monday','tuesday','wednesday','thursday','friday','saturday','sunday')
    day = input("Enter name of the day of week to filter by, or 'all' to apply no day filter: ").lower()
    while day not in day_list:
            print("Day is not on the list.")
            day = input("Enter name of the day of week to filter by, or 'all' to apply no day filter: ").lower()
            
    print('-'*40)
    return city, month, day
    
def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
 # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    common_month = df['month'].mode()[0]
    print('Most Common Month:', months[common_month-1])

    # TO DO: display the most common day of week

    common_day = df['day_of_week'].mode()[0]
    print('Most Common Day:', common_day)

    # TO DO: display the most common start hour

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # find the most common hour
    common_hour = df['hour'].mode()[0]

    print('Most Common Hour:', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print('Most Common Start Station:', start_station)

    # TO DO: display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print('Most Common End Station:', end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + " to " + df ['End Station']
    Freq_comb = df['combination'].mode()[0]
    print('Most frequent combination of start station and end station trip:', Freq_comb)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    
    Total_travel_time = df['Trip Duration'].sum()
    print('Total travel time:', Total_travel_time)

    # TO DO: display mean travel time

    Mean = df['Trip Duration'].mean()
    print('Average trip duration:', Mean)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(df['User Type'].value_counts())

    # TO DO: Display counts of gender
    while city != 'washington':
        print(df['Gender'].value_counts())
    
    # TO DO: Display earliest, most recent, and most common year of birth
        min_dob = df['Birth Year'].min()
        print('Earliest year of birth:', int(min_dob))

        max_dob = df['Birth Year'].max()
        print('Most recent year of birth:', int(max_dob))

        common_dob = df['Birth Year'].mode()[0]
        print('Most common year of birth:', int(common_dob))
        break
    else:    
        print('Washington.csv does not have "Gender" column')
        print('Washington.csv does not have "Birth Year" column')
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_rows(df):
    """Displays 5 rows of data based on user input """
    display = input('Would you like to see 5 rows of data? Enter yes or no:').lower()
    start_loc = 0
    while (display == 'yes'):
        print(df.iloc[start_loc:start_loc + 5])
        start_loc = start_loc + 5
        display = input("Would you like to see the next 5 rows?: ").lower()
        if display != 'yes': 
            break
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_rows(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
