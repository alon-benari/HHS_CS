import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np
import jsonschema

class CS:
    '''
    Set of methods 
    '''
    def __init__(self):
        self.data = pd.read_csv('breach_report.csv')
        self.data['Count'] = np.ones(self.data.shape[0])
        self.data['SubmissionMonth'] = self.data['Breach Submission Date'].apply(lambda x: pd.Timestamp(x).month)
        self.data['SubmissionDate'] = self.data['Breach Submission Date'].apply(lambda x: pd.Timestamp(x).date())
        self.data['SubmissionYear'] = self.data['Breach Submission Date'].apply(lambda x: pd.Timestamp(x).year)
        self.data['SubmissionMonth'] = self.data['Breach Submission Date'].apply(lambda x: pd.Timestamp(x).month)
        self.data['SubmissionYearDay'] = self.data['Breach Submission Date'].apply(lambda x: pd.Timestamp(x).dayofyear)

    def daily_event(self, year):
        '''
        return a summary statistics for daily breach counts
        '''
        df = cs.data[(cs.data['SubmissionYear'] == year)]
        counts = df[['Count','SubmissionYearDay']].groupby('SubmissionYearDay').count()
        
        return counts

    def covered_entity(self, year):
        '''
        Return statistics regarding rate of covered entities
        '''
        df = cs.data[(cs.data['SubmissionYear'] == year)]
        return df[['Covered Entity Type','Count']].groupby('Covered Entity Type').count() 

    def breach_type(self, year):
        '''
        stats on breach type
        '''
        df = cs.data[(cs.data['SubmissionYear'] == year)]
        return df[['Type of Breach','Count']].groupby('Type of Breach').count()

    def by_state(self,year):
        '''
        Return counts of by state
        '''
        df = cs.data[(cs.data['SubmissionYear'] == year)]
        return df[['State','Count']].groupby('State').count()

    def  us_population(self):
        '''
        Return state and population for the US.
        '''
        f = open('USpopulatio.json')
        data = json.load(f)
        return return df[['Type of Breach','Count']].groupby('Type of Breach').count()

    
        
        



##run
cs = CS()
# daily events
# daily_event= cs.daily_event(2023)
# fig,(ax0,ax1) = plt.subplots(1,2)
# ax0.set_xlabel('daily count')
# ax0.hist(daily_event, bins = 36)
# ax1.set_xlabel('count')
# ax1.boxplot(daily_event.Count)

# covered entities
# covered = cs.covered_entity(2024)
# fig, ax = plt.subplots(1,1,figsize = (10,8))
# ax.set_title('breach count by  entities')
# covered.plot.barh(ax = ax)
# plt.show()

#Type of breach
breach_type = cs.breach_type(2024)
fig, ax = plt.subplots(1,1,figsize = (10,8))
ax.set_title('breach count by  entities')
breach_type.plot.barh(ax = ax)
plt.show()

#
