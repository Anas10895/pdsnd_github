import time
import pandas as pd
import numpy as np
import datetime
import statistics as st


CITY_DATA = {'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv'}


def get_filters():

    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("please chose a city from chicago, new york , washington").lower()
        if city in("chicago","new york","washington"):
            break
        else:
            print("Sorry Invalid input please chose again")
            continue

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("please chose a month from:  all , january, february, march, april, june, may, june").lower()
        if month  in ("all", "january", "february", "march", "april", "june", "may", "june"):
            break
        else:
            print("Sorry Invalid input please chose again")
            continue

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("please chose a day: sunday, moonday, tuesday, wednsday, thursday, friday, saturday, all").lower()
        if day in ("sunday", "moonday", "tuesday", "wednsday", "thursday", "friday", "saturday", "all"):

            break
        else:
            print("Sorry Invalid input please chose again")
            continue

     

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
#     Loads data for the specified city and filters by month and day if applicable.
    df =pd.read_csv(CITY_DATA[city])

    
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["End Time"]= pd.to_datetime(df["End Time"])

# # (str) month - name of the month to filter by, or "all" to apply no month filter
    if month != "all":
                   months = ['january', 'february', 'march', 'april', 'june', 'may', 'june']
                   month = months.index(month) + 1
                   df = df[df["Start Time"].dt.month == month]
# #(str) day - name of the day of week to filter by, or "all" to apply no day filter
    if day != "all":
                   df = df[df["Start Time"].dt.weekday_name == day.title()]
    print(df.head())
    return df


def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time= time.time()

    # TO DO: display the most common month
    if (month == "all"):
            mostMonth = df["Start Time"].dt.month.value_counts().idxmax()
            print("The most common month is: ", str(mostMonth))
    # TO DO: display the most common day of week
    if (day == "all"):
            mostDay = df["Start Time"].dt.weekday_name.value_counts().idxmax()
            print("The most common Day is: ", str(mostDay))

    # TO DO: display the most common start hour
    mostHour = df["Start Time"].dt.hour.value_counts().idxmax()
    print("The most common huor is: ", str(mostHour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    mostStartStaion = st.mode(df["Start Station"])
    print("The most used start staion is: {}".format(mostStartStaion))
    # TO DO: display most commonly used end station
    mostEndStaion = st.mode(df["End Station"])
    print("The most used end staion is: {}".format(mostEndStaion))

    # TO DO: display most frequent combination of start station and end station trip
    mostCombination = df["Start Station"].astype(str)+" and "+ df["End Station"].astype(str)
    mostFrequent = mostCombination.value_counts().idxmax()
    print("The most Frequent trip is: {}".format(mostFrequent))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time=time.time()

    # TO DO: display total travel time
    totalTime = df["Trip Duration"].sum()
    time1 = totalTime
    day =  time1 // (24*3600)
    time1 = time1 % (24*3600)
    hour = time1 // 3600
    minutes = time1 // 60
    time1 %= 60
    seconds = time1 
    print("Total travel time is {} days {} hours {} minutes {} seconds ".format(day, hour, minutes, seconds))
    
    # TO DO: display mean travel time

    meanTime = df["Trip Duration"].mean()
    time1 = meanTime
    hour = time1 // 3600
    minutes = time1 // 60
    time1 %= 60
    seconds = time1 
    print("Mean travel time is  {} hours {} minutes {} seconds".format(hour, minutes, seconds))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time=time.time()

    # TO DO: Display counts of user types
    userTypes=df["User Type"].value_counts()
    print("user Tybes : ", userTypes)

    # TO DO: Display counts of gender
    if "Gender" in df.columns:
        genderCounts=df["Gender"].value_counts()
        print("the Count of user gender is: ", genderCounts)




    # TO DO: Display earliest, most recent, and most common year of birth
    if ("Birth Year" in df):
        earliestYear=df["Birth Year"].min()
        mostRecentYear=df["Birth Year"].max()
        mostCommonYear=df["Birth Year"].mode()[0]

        print("The erliest birth year is : ", earliestYear)
        print("The most recent Year of birth is: ", mostRecentYear)
        print("The Most common year of birth is: ", mostCommonYear)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    

def rawData(df):

    print("Do you wnat to see more Data ?")
    count = 0
    while True:
        more_data = input("More data Yes or No?").lower()
        if more_data == "yes":
            print(df.iloc[count:count+5])
            count += 5
        else:
            break




def main():
    while True:
        city, month, day=get_filters()
        df=load_data(city, month, day)

        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        rawData(df)

        restart=input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
