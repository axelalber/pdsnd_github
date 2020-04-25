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
    
    while True: 
        i = input('Choose city, chicago, new york city, or washington\n').lower()
        if i == 'chicago' or i == 'new york city' or i == 'washington':
            break;
        else:
            print('Not a valid input')
    city = i
    # TO DO: get user input for month (all, january, february, ... , june)
    while True: 
        i = input('Choose month, all, or month between january - june\n').lower()
        if i == 'all' or i == 'january' or i == 'february' or i == 'march' or i == 'april' or i == 'may' or i == 'june':
            break;
        else:
            print('Not a valid input')
    month = i

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True: 
        i = input('Choose day, or all\n').lower()
        if i == 'all' or i == 'monday' or i == 'tuesday' or i == 'wednesday' or i == 'thursday' or i == 'friday' or i == 'saturday' or i == 'sunday':
            break;
        else:
            print('Not a valid input')
    day = i
    
    print('-'*40)
    return city, month, day

import pandas as pd


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - pandas DataFrame containing city data filtered by month and day
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
        month = months.index(month)+1
    
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
    common_month = df['month'].mode()[0]
    print('Month: {}'.format(common_month))
    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('Day: {}'.format(common_day))
    # TO DO: display the most common start hour
    common_hour = df['Start Time'].dt.hour.mode()[0]
    print('Hour: {}'.format(common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start = df['Start Station'].mode()[0]
    print('Most popular start station: {}'.format(common_start))

    # TO DO: display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print('Most popular end station: {}'.format(common_end))

    # TO DO: display most frequent combination of start station and end station trip
    common_combo = (df['Start Station']+' - '+df['End Station']).mode()[0]
    print('Most popular trip: {}'.format(common_combo))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print('Total time: {} seconds'.format(int(total_time)))
    # TO DO: display mean travel time
    mean = total_time / len(df.index)
    print('Mean time: {} seconds'.format(int(mean)))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)
    
    # TO DO: Display counts of gender
    if not 'Gender' in df.columns:
        print('No data for gender in Washington')
    else:
        gender = df['Gender'].value_counts()
        print(gender)
    

    # TO DO: Display earliest, most recent, and most common year of birth
    if not 'Birth Year' in df.columns:
        print('No data for birth year in Washington')
    else:
        oldest = df['Birth Year'].min()
        youngest = df['Birth Year'].max()
        common = df['Birth Year'].mode()[0]
    
        print('Earliest birth year: {}\nMost recent birth year: {}\nMost common birth year: {}'.format(int(oldest),int(youngest),int(common)))
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def raw_data(df):
    current = 0
    end = 5
    while True:
        if current == 0:
            i = input('Do you want to see 5 rows of raw data? Enter yes or no.\n').lower()
        else:
            i = input('Do you want to see 5 more rows? Enter yes or no.\n').lower()
        if i != 'yes':
            break
        else:
            print(df.iloc[current:end])
            current = end
            end += 5
            

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
