#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 16:19:07 2017

@author: yifan
"""

import requests
import json
import sys

def main():
    
# Get data forms from the given data API key and then we parse the pre-processed data as a json file
    raw = requests.get('https://api.typeform.com/v1/form/PfSNFM?key=ac83034cfa742c0f79c26e9a612b4ba7e2aa0d3d')
    data = raw.json()
    
    with open('typeform_data.json','w') as file:
        json.dump(data,file)
       
    with open('typeform_data.json','r') as file:
        records = json.load(file)
        
    # Check the first-layer data structure of the obtained json data file to obtain all the keys of 
    # the first-layer:
    for i in records:
        print i
    # Store all the values corresponding to the first-layer keys into specific objects   
    stats = records['stats']
    http_status = records['http_status']
    questions = records['questions']
    responses = records['responses'] # The main object of our concern here.
    
    #Then we are able to obtain the keys of the next-layer of the data structure, responses.
    print type(responses) # responses is a list, NOT a dict !!!
    
    for each_dict in responses:
        print each_dict.keys()
    
    # Declare the necessary responses objects (as lists) for the "answers" and the "metadata" two parts.
    # For the response objects from the answers
    list_choice = []
    date = []
    textarea = []
    yesno = []
    number = []
    # For the response objects from the metadata
    network_id = []
    platform = []
    referer = []
    user_agent = []
    date_submit = []
    date_land = []
    browser = []
    
    # create the responses objects:
    for each_dict in responses:
        
        # iterate the loop by the keys
       for i in each_dict:
           
           if i == "answers":
               # We need to check if all the answer keys actually exist in all the responses,
               # if some keys dont exist at all, we produce "NaN" for that new key.
               # Otherwise, we simply append the responses values to the responses objects that we have created.
                if "list_46100308_choice" in each_dict[i]:
                    list_choice.append(each_dict[i]["list_46100308_choice"])
                elif ("list_46100308_choice" in each_dict[i]) == False :
                    each_dict[i]["list_46100308_choice"]= "NaN"
                    list_choice.append(each_dict[i]["list_46100308_choice"])
    
                
                if "date_46098446" in each_dict[i]:
                     date.append(each_dict[i]["date_46098446"])
                elif ("date_46098446" in each_dict[i]) == False:
                     each_dict[i]["date_46098446"]= "NaN"
                     date.append(each_dict[i]["date_46098446"])
    
                    
                if "textarea_46100513" in each_dict[i]:
                    textarea.append(each_dict[i]["textarea_46100513"])
                elif ("textarea_46100513" in each_dict[i]) == False :
                    each_dict[i]["textarea_46100513"]= "NaN"
                    textarea.append(each_dict[i]["textarea_46100513"])
    
                    
                if "yesno_46099317" in each_dict[i]:
                    yesno.append(each_dict[i]["yesno_46099317"])
                elif ("yesno_46099317" in each_dict[i]) == False :
                    each_dict[i]["yesno_46099317"]= "NaN"
                    yesno.append(each_dict[i]["yesno_46099317"])
    
    
                if "number_46099137" in each_dict[i]:
                    number.append(each_dict[i]["number_46099137"])
                elif ("number_46099137" in each_dict[i]) == False :
                    each_dict[i]["number_46099137"]= "NaN"
                    number.append(each_dict[i]["number_46099137"])
    
                    
    # As for the metadata responses, all we need to do is:
    # we simply append the responses to the metadata responses objects that we have created.
    # Namely, we dont need to make any changes to the relavant fields of the original json file,
    # Thus, using iterator defined in the dict will be much faster.
    for each_dict in responses:
        
       for k,v in each_dict.iteritems():
                      
           if k == "metadata":
               
               for k1,v1 in v.iteritems():
                   
                   if k1 == "network_id":
                       network_id.append(v1)
                   elif k1 == "platform":
                       platform.append(v1)
                   elif k1 == "referer":
                       referer.append(v1)
                   elif k1 == "user_agent":
                       user_agent.append(v1)
                   elif k1 == "date_submit":
                       date_submit.append(v1)
                   elif k1 == "date_land":
                       date_land.append(v1)
                   elif k1 == "browser":
                       browser.append(v1)
    
    # Sanity Check on the size of the processed data structures corresponding to responses objects
    # by doing this we have directly detected that the sizes of responses onjects didnt match initially.
    print len(list_choice)
    print len(date)
    print len(textarea)
    print len(yesno)
    print len(number)
    
    print len(network_id)
    print len(platform)
    print len(referer)
    print len(user_agent)
    print len(date_submit)
    print len(date_land)
    print len(browser)
    
    #output the final processed data structure into a csv file
    orig_stdout = sys.stdout #temporarily save the standard output
    file = open('output.csv', 'w')
    sys.stdout = file
    # each response object that we have created occupies one single column; totally, they form a single table
    # The spanning of columns are enabled upon calling zip() function
    for i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12 in zip(list_choice,date,textarea,yesno,number,network_id,platform,referer,user_agent,date_submit,date_land,browser): 
        print '{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}\t{10}\t{11}'.format(list_choice,date,textarea,yesno,number,network_id,platform,referer,user_agent,date_submit,date_land,browser)
    
    sys.stdout = orig_stdout 
    file.close()
       

if __name__ == "__main__":
    main()
            



