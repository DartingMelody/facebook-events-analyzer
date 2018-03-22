import os
import re
import matplotlib.pyplot as plt
import numpy as np
#Open file
file_path  = os.path.join('html','events.htm')
f = open(file_path, "r")
file_data = f.read()

#Get Data from file
matchObj = re.search(r'<h2>Events</h2><ul>(<li>(.+?)</li>)</ul>', file_data)
events_data_html_formatted = matchObj.group(1)
no_replies = int(events_data_html_formatted.count("No reply"))
maybe = int(events_data_html_formatted.count("Maybe"))
attending = int(events_data_html_formatted.count("Attending"))

#Setting x and y values of the plot
label = ["No reply", "Maybe", "Attending"]
values = [no_replies, maybe, attending]

# Plotting the graph
index = np.arange(len(label))
plt.bar(index, values )
plt.xlabel('Event Status', fontsize=10)
plt.ylabel('Count', fontsize=10)
plt.xticks(index, label, fontsize=10)
plt.title('Status of replies for events')
plt.show()
