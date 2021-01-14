import pandas as pd
import re

class dfp:
    def storage(self):
        try:
            df = pd.read_csv('..\\data\\in\\df_storage.csv', encoding='Windows-1251', sep=';')
            df = df.rename(columns={'Название ': 'name', 'Артикул ': 'art', 'ID ': 'id'})
            df = df[['id', 'art', 'name']]
        except:
            df = "Error read *.csv file!"

        return df
    def components(self, df, group_name):
        #self.__select(group_name, "234 Резистор Конден ыва олма ")
        #dftmp = df.name.apply(lambda x: self.__select(group_name, x))
        #print(dftmp)
        pass


    def __select(self, group_name, name):
        cont = group_name['contains']
        #ncont = group_name['not_contains']
        if name and cont:
            if ' ' in cont: cont = re.split(r' ', cont)
            if ' ' in name: splname = re.split(r' ', name.lower())
            if any(word in splname for word in cont):
                return name
                #print(name)




        '''
        for word in str:
            for rul in con:
                if word.lower() == rul:
                    #for nrul in ncon:
                        if word.lower() == nrul:
                            break
                        else:
                            print(x)
        '''