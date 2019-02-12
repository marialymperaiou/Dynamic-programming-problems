# Given N jobs with their starting time, ending time and value, find the maximum
# profit of non-overlapping jobs

# 1st option: they all have the same values
def job_scheduling_1(start, finish,schedule):
    # first, we need to sort by finish time
    # fix the starting times accordingly
    start=[x for y, x in sorted(zip(finish,start))]
    finish=sorted(finish)
    print('Start times:',start)
    print('Finish times:', finish)
    j = 0                   #starting from the first job
    schedule.append(j)      #we take it, as it has the smallest finish time
    for i in range(len(finish)):
        #check if a job starts the same time, or after another job finishes
        if start[i]>=finish[j]:
            schedule.append(i)      #then, consider this job as the next in the list
            j=i                     #and from now on, we check with this job

    return schedule

start = [5,1,8,0,1,5]
finish = [9,2,9,6,4,7]
schedule = []
print(job_scheduling_1(start, finish, schedule))

# 2nd option: each job has a different value
def job_scheduling_2(start, finish, values, schedule):
    values=[x for z, x in sorted(zip(finish,values))]
    start=[x for y, x in sorted(zip(finish,start))]
    finish=sorted(finish)
    print('Start times:',start)
    print('Finish times:', finish)
    print('Values:', values)
    
    #create optimal solution table
    total_profit = [0 for x in range(len(values))]
    total_profit[0]=values[0]           #we take the first job
    job_list = []                       #we keep track of the chosen jobs
    
    for i in range(1,len(values)):
        temp = values[i]                #keep the current value
        flag = True
        j = i-1                         #check from the previous job until the beginning
        while(flag and j>=0):
            if finish[j]<=start[i]:     #if this previous job is not overlapping
                k = j                   #keep this job
                flag = False            #this will exit the loop
            else:
                k = -1                  #an invalid value will indicate that there is not non-overlapping job
            j -= 1  # check the job before
        if k!=-1:   #if no overlapping job
            temp += total_profit[k]

        #either you include this profit, or not
        total_profit[i] = max(temp, total_profit[i-1])
        if temp < total_profit[i-1]:
            if i-1 not in job_list:     #check if the job has been already inserted
                job_list.append(i-1)
        else:
            job_list.append(i)
            
    return total_profit[len(values)-1], job_list

values = [6,4,5,2,10,6]
print(job_scheduling_2(start, finish, values, schedule))