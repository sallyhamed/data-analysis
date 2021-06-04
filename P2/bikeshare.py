

# import important Libraries

import time
import pandas as pd


# Load  data.
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


def check_input(input_str,input_type):
    while True:
        user_input = input(input_str).casefold()
        try:
            if user_input in ['chicago','new york city', 'washington'] and input_type==1:
                break
            elif user_input in ['all', 'january', 'february', 'march', 'april','may','june'] and input_type==2:
                break
            elif user_input in ['all', 'monday', 'tuesday',' wednesday', 'thusday','friday','saturday','sunday'] and input_type==3:
                break
            else:
               print('Try again invalid answer')
        except ValueError:
            print('Wrong input data')
    return user_input
       
        
              
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    
    
    # get user input for city (chicago, new york city, washington). 
    city = check_input('would you like to see data for chicago, new york city,or washington?\n ',1)
 
    # get user input for month (all, january, february, ... , june)
    month = check_input('which month? all, january, february, march, april,may,or june ? \n',2)
    
    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = check_input('which day? all,monday,tuesday,wednesday,thursday,friday,saturday,sunrday?\n ',3)  
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

    # extract month , day of week ,hour and start end station from Start Time to create new columns

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    df['star_end_station'] = df['Start Station'] + ' to ' + df['End Station']
    

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

def show_data(df):
    """
   prompt the user if they want to see 5 lines of raw data. 
   display that data if the answer is 'yes', and continue these prompts and displays until the user says 'no'.
    """
    print(df.sample(5))
    i=0
    ask = input('\nWould you like to showe more data? Enter yes or no.\n')
     
    while True:
       if ask.lower() != 'yes':
           break
       print(df[i:i+5])
       ask = input('\nWould you like to showe more data? Enter yes or no.\n')
       
       i += 5 
 
       
                  
                   
    

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # find the most popular month
    popular_month = df['month'].mode()[0]
    print('Most Popular Start Month:', popular_month)
    
    # find the most popularday
    popular_day = df['day_of_week'].mode()[0]
    print('Most Popular Start Day:', popular_day)
    
    # find the most popular hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    # find the most popular Start Station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most commonly used start station:', popular_start_station)
    print(' '*40)
    
    # find the most popular End Station
    popular_end_station = df['End Station'].mode()[0]
    print('Most commonly used end station:', popular_end_station )
    print(' '*40)
    
    # find the most popular star_end_station
    #popular_start_end_station = df.groupby(['Start Station','End Station']).size().nlargest(1)
    
    popular_start_end_station =  df['star_end_station'].mode()[0]
    print('Most commonly used start station and end station:',popular_start_end_station)
    print(' '*40)        
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def trip_duration_stats(df):
    """Displays statistics on the most popular stations and trip."""
    

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    # display total travel time
    total_time = df['Trip Duration'].sum()
    print('Total travel time:',total_time)
    
     # display mean travel time
    average_time = df['Trip Duration'].mean()
    print('Mean travel time:', average_time)
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""


    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)
    
    
    #no gender or birthday in washington
    if city !='washington':
        
         # Display counts of gender
         gender = df['Gender'].value_counts()
         print(gender)
         
         # Display earliest, most recent, and most common year of birth
         earliest_year = df['Birth Year'].min()
         print('Most earliest year:', earliest_year )
    
         recent_year = df['Birth Year'].max()
         print('Most recent year:', recent_year )
    
         popular_year = df['Birth Year'].mode()[0]
         print('Most common year:', popular_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)




def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        show_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break        




if __name__ == "__main__":
	main()

