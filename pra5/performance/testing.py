import os

import requests
import pandas as pd
from datetime import datetime

# to create box plots
import seaborn as sns
import matplotlib.pyplot as plt

# configure plots
sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (8, 6)

# Number of requests to send
ITERATIONS = 100

# save outputs to specified directory
OUTPUT_DIR = './output'
os.makedirs(OUTPUT_DIR, exist_ok=True)

# URL and headers from your cURL request
url = "http://127.0.0.1:5000/predict"
# url = "http://test-app-env.eba-fctwsrc4.us-east-1.elasticbeanstalk.com/predict"
headers = {
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
    "Cookie": "session=eyJjc3JmX3Rva2VuIjoiOTEzMzA2NmRhM2JhMTZhMmUwNzY4NjlkMTY2NDg1ODBhNTdhOTk4NyJ9.ZxbdCA.Y5xUWBhg6i2TktuaF0pDlexpxv0",
    "Origin": "http://test-app-env.eba-fctwsrc4.us-east-1.elasticbeanstalk.com",
    "Pragma": "no-cache",
    "Referer": "http://test-app-env.eba-fctwsrc4.us-east-1.elasticbeanstalk.com/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
}

test_data = [
    { "text": "Young voters in key election battlegrounds are being recommended fake AI-generated videos featuring party leaders, misinformation, and clips littered with abusive comments, the BBC has found.",
     "label": "REAL"
     },
    {
    "text": "The head of the Canadian Broadcasting Corp. is facing scrutiny from members of a House of Commons committee for her roughly $6,000 worth of travel and hotel expenses at the Paris Olympics this past summer.",
    "label": "REAL"},
    { "text": "Local Cat Becomes Overnight's Sensation After Saving a Child from a Dog Attack",
     "label": "FAKE"},
    { "text": "In a shocking study released by the Institute of Absurd Science, researchers have concluded that chocolate can be classified as a vegetable because it comes from cocoa beans. This revelation has led to a nationwide surge in chocolate sales, with the government now recommending three servings of chocolate daily for a balanced diet. Health experts are still debating how to work this into the food pyramid.", "label": "FAKE"}
]

plot_data = []

for test_id, test  in enumerate(test_data):
    print('Test number:', test_id)
    print(test)

    # List to store log information
    log_data = []

    # Sending 100 requests
    for i in range(ITERATIONS):
        # Timestamp when request is sent
        request_time = datetime.now()
        
        # Send the request
        try:
            response = requests.post(url, headers=headers, json=test, verify=False)  # verify=False to ignore SSL warnings
            response_time = datetime.now()

            print('response prediciton', response.json().get('prediction'))

            response_duration = (response_time - request_time).total_seconds()
            
            # Log request and response details
            log_data.append({
                "request_time": request_time,
                "response_time": response_time,
                "response_duration_seconds": response_duration,
                "predict": response.json().get('prediction'),
                "label": test["label"],
            })
            
            print(f"Request {i+1} sent successfully. Response received.")
        except Exception as e:
            print(f"Request {i+1} failed: {e}")

    # Create a DataFrame from the log data
    df = pd.DataFrame(log_data)

    # Mapping categorical to numerical values
    df['predict_numeric'] = df['predict'].map({'FAKE': 0, 'REAL': 1})
    df['label_numeric'] = df['label'].map({'FAKE': 0, 'REAL': 1})

    # add plot data based on predict_numeric
    test_plot_data = df['predict_numeric'].tolist()
    plot_data.append(test_plot_data)

    # calculate accuracy and write to a file
    df['correct'] = df['predict_numeric'] == df['label_numeric']
    accuracy = df['correct'].mean()

    with open(os.path.join(OUTPUT_DIR, f'test_{test_id}_acc.txt'), 'w') as acc_file:
        acc_file.write(f"Test {test_id} Accuracy: {accuracy:.4f}\n")

    # Save DataFrame to CSV
    csv_file = os.path.join(OUTPUT_DIR, f'test_{test_id}_log.csv')
    df.to_csv(csv_file, index=False)

    print(f"Log saved to {csv_file}.")

    # # Create a box plot for each predictions
    # plt.figure(figsize=(12, 6))
    # sns.boxplot(data=df[['predict_numeric', 'label_numeric']])
    # plt.xticks([0, 1], ['Predictions', 'True Labels'])
    # plt.ylabel('Binary Value')
    # plt.title(f'Test {test_id}: Predictions and True Labels')

    # plt.savefig(os.path.join(OUTPUT_DIR, f'test_{test_id}_plot.png'), dpi=300, bbox_inches='tight')

    # plt.show()

# create box plot for all tests
sns.boxplot(data=plot_data)
plt.xticks(labels=['Test 0', 'Test 1', 'Test 2', 'Test 3'], ticks=[0, 1, 2, 3])
plt.ylabel('Predicted Value')
plt.title(f'Predicted Values for Each Test')

plt.savefig(os.path.join(OUTPUT_DIR, f'all_tests_plot.png'), dpi=300, bbox_inches='tight')

plt.show()