# import pandas as pd

# # List of vishing (phone call scam) scenarios
# scenarios = [
#     # Original scenarios
#     "John calls Emily claiming to be from her credit card issuer's fraud department. He tells her that suspicious charges have been detected and asks her to confirm her card number and CVV to resolve the issue.",
#     "A caller identifies as Mike from a well-known tech company, telling Samantha that her computer has a virus. He asks for remote access to her computer and requests her credit card details for a fake antivirus software.",
#     "Rachel calls Tom, claiming to be from the Social Security Administration. She says his Social Security number has been compromised and needs verification. To fix the issue, she requests his personal information and bank account details.",
#     "Linda calls Mark, claiming to be from his mortgage company. She offers him a temporary mortgage relief program and asks for his mortgage account number and other personal information to set it up.",
#     "Jessica calls Alan, pretending to represent his credit card company. She tells him that he's been enrolled in a rewards program and requests his credit card number to apply the benefits.",
#     "Oscar contacts Sarah, claiming to represent her insurance company. He states that her policy needs updating and asks for her policy number and other personal information to update her records.",
#     "Tom calls Lucy, pretending to represent her bank, and offers her a low-interest loan. To proceed, he asks for her bank account details and other sensitive information.",
#     "Daniel contacts Kate, claiming to be from the Internal Revenue Service (IRS). He says that she owes back taxes and must pay immediately to avoid legal consequences. He asks for her bank details to process the payment.",
#     "Sam calls Laura, pretending to represent a government agency offering a grant for small businesses. He asks for her business bank account details to deposit the grant funds.",
#     "Diana contacts John, pretending to represent a popular social media platform. She says his account needs to be verified and asks for his login credentials to proceed.",

#     # Additional scenarios
#     "Matthew contacts Paula, claiming to represent her home security company. He offers a free system upgrade but needs her account number and address to schedule installation.",
#     "Stephanie calls Brian, pretending to be from his health insurance provider. She says there's an issue with his current plan and asks for his policy number and other personal information to update his coverage.",
#     "Emma calls Chris, offering credit card debt relief. To start the process, she asks for his credit card numbers and other personal information.",
#     "James calls Monica, pretending to represent her bank. He tells her about a new premium account with exclusive benefits and requests her current account number to upgrade her account.",
#     "Oliver contacts Helen, pretending to represent a well-known charity. He asks for a donation and provides a phone number to call back with credit card information.",
#     "Benjamin calls Alice, claiming to be a debt collector. He says she has an outstanding loan and threatens legal action if she doesn't pay immediately, requesting her bank account details for payment.",
#     "Natalie calls Andrew, offering a discounted travel package. She asks for his credit card information to confirm the booking and secure the special rate.",
#     "Alexander contacts Susan, pretending to represent an investment firm. He offers an exclusive investment opportunity and asks for her bank account details to proceed.",
#     "Samantha contacts Michael, claiming to represent a university. She offers him a scholarship but needs his personal information and bank details to process the scholarship funds.",
#     "Patrick calls Carol, pretending to represent a popular magazine. He offers her a subscription renewal at a discounted rate and requests her credit card details to proceed.",

#     # More scenarios
#     "William contacts Mary, offering home repair services. He asks for her address and credit card details to schedule a consultation and process the initial fee.",
#     "Charlotte calls Robert, pretending to represent his mobile service provider. She offers a plan update with better rates and asks for his account details to proceed.",
#     "Victoria calls Kevin, claiming to represent his auto insurance company. She asks for his policy number and other personal information to verify his coverage.",
#     "David contacts Jenna, offering a discounted car rental. He asks for her credit card details to confirm the booking and secure the special rate.",
#     "Megan contacts George, offering a gift card for his favorite store. To receive it, she asks for his address and credit card details to pay for shipping.",
#     "Laura contacts Anthony, offering tickets to a popular sports event. She asks for his credit card details to confirm the booking and secure the tickets.",
#     "Peter calls Sandra, claiming to represent her local utility company. He asks for her address and other personal information to schedule maintenance and avoid service disruption.",
#     "Amanda contacts Greg, offering financial advice and portfolio management services. She asks for his bank account details to begin the investment process.",
#     "Daniel calls Nancy, offering a discount on her favorite online store. He asks for her credit card details to apply the discount and complete the purchase.",
#     "Rebecca contacts Bruce, claiming to represent a streaming service. She tells him that his subscription is being canceled and asks for his credit card details to prevent the cancellation and keep his subscription active.",
# ]

# # Create a list of labels (assuming all are fraudulent scenarios)
# labels = ["Fraud"] * len(scenarios)

# # Create a DataFrame with the scenarios and labels
# df = pd.DataFrame({
#     "scenario": scenarios,
#     "label": labels
# })

# # Save the DataFrame to a CSV file
# output_csv_path = 'fraud_scenarios.csv'  # Update with your desired file path
# df.to_csv(output_csv_path, index=False)  # Save to CSV without row index



# import pandas as pd

# # List of phishing (email scam) scenarios
# phishing_scenarios = [
#     "Samuel sends an email to Alice, appearing to be from her bank. The email claims there's been suspicious activity on her account and asks her to click on a link to verify her identity. The link leads to a phishing site designed to steal her credentials.",
#     "Emma sends an email to Ben, appearing to be from a popular online retailer. The email claims he's eligible for a refund on a recent purchase and provides a link to claim it. The link leads to a phishing site designed to steal his personal information.",
#     "Liam sends an email to Clara, claiming to be from a shipping company. The email states that her package couldn't be delivered and provides a link to reschedule the delivery. The link leads to a phishing site.",
#     "Charlotte sends an email to David, pretending to represent a reputable company offering a job opportunity. The email asks for his banking information for payroll setup, but it's a phishing attempt designed to steal his information.",
#     "Olivia sends an email to Emily, pretending to represent a popular social media platform. The email claims her account needs to be verified and includes a link to reset her password. The link leads to a phishing site.",
#     "William sends an email to Mark, appearing to be from his software provider. The email prompts him to download an attachment for a critical software update, but the attachment contains malware designed to steal his personal information.",
#     "Sophia sends an email to Frank, claiming to be from a government agency offering a tax refund. The email provides a link to submit his banking details to receive the refund, but it's a phishing attempt.",
#     "James sends an email to Lucy, pretending to represent a subscription-based service. The email claims her subscription is about to expire and asks her to click on a link to renew. The link leads to a phishing site designed to steal her credit card details.",
#     "Ava sends an email to George, claiming to represent a charity organization. The email asks for a donation and provides a link to donate. The link leads to a phishing site designed to steal his financial information.",
#     "Michael sends an email to Nancy, pretending to represent her workplace's IT department. The email states there's a security update and provides an attachment to download, but the attachment contains malware designed to steal her personal and financial information.",
#     "Elijah sends an email to Robert, pretending to represent his health insurance provider. The email claims he's eligible for a refund due to overpayment and provides a link to submit his banking information to receive it, but it's a phishing attempt.",
#     "Isabella sends an email to Anthony, offering investment opportunities and requesting his bank account details to proceed. The email appears to come from a reputable financial advisor, but it's a phishing scam.",
#     "Mia sends an email to Peter, claiming to be from a loan company. The email states that his loan has been approved and asks him to provide his bank account details to receive the funds. The link leads to a phishing site designed to steal his information.",
#     "Lucas sends an email to Sandra, claiming she's won a prize in a contest or lottery. The email asks for her bank account details or credit card information to claim the prize, but it's a phishing attempt.",
#     "Zoe sends an email to Kevin, pretending to represent a reputable company. The email invites him to participate in a customer satisfaction survey and provides a link. The link leads to a phishing site designed to steal his personal information.",
#     "Harper sends an email to Carol, pretending to be from a well-known tech company. The email claims there's a problem with her computer and provides a link to fix it, but the link leads to a phishing site designed to steal her information.",
#     "Ethan sends an email to Monica, claiming she's won a lottery prize. The email asks for her personal information and bank account details to process the winnings, but it's a phishing attempt.",
#     "Aria sends an email to Bruce, offering discounted vacation packages and requesting his credit card details to secure the booking. The email appears to be from a travel agency, but it's a phishing scam.",
#     "Aiden sends an email to Jenna, pretending to represent a popular streaming service. The email claims there's a billing issue and asks her to click on a link to update her payment information. The link leads to a phishing site designed to steal her credit card details.",
#     "Liam sends an email to Mary, pretending to represent a government agency offering financial assistance due to a pandemic. The email provides a link to submit her banking information to receive the assistance, but it's a phishing scam.",
#     "Noah sends an email to Paul, pretending to represent a real estate agency. The email offers an exclusive real estate deal and asks for his credit card information to secure the deal. The link leads to a phishing site designed to steal his payment information.",
#     "Oliver sends an email to Claire, pretending to represent a streaming service. The email claims her subscription is being canceled and asks her to click on a link to prevent the cancellation. The link leads to a phishing site designed to steal her credit card details.",
#     "Amelia sends an email to Greg, pretending to represent an online subscription-based service. The email claims he's been subscribed to a premium service and asks him to confirm his subscription by clicking on a link, but the link leads to a phishing site designed to steal his information.",
#     "Jack sends an email to Julia, pretending to represent a popular online payment platform. The email asks her to click on a link to verify her account information, but the link leads to a phishing site designed to steal her credentials.",
#     "Henry sends an email to Betty, claiming to represent her local utility company. The email states that there's an unpaid bill and asks her to click on a link to make the payment, but the link leads to a phishing site.",
#     "Alexis sends an email to Chris, claiming to represent a university offering a scholarship. The email asks for his personal information and bank account details to process the scholarship, but it's a phishing attempt.",
#     "Dylan sends an email to Emily, offering tickets to a popular sports event at a discounted rate. The email asks her to enter her credit card details to confirm the purchase, but it's a phishing scam designed to steal her payment information.",
#     "Sebastian sends an email to Claire, claiming to represent her mobile carrier. The email offers a plan update with better rates and asks her to enter her account details to proceed, but it's a phishing attempt.",
#     "Madison sends an email to Nick, offering a discount on his favorite online store. The email asks him to click on a link to claim the discount, but the link leads to a phishing site designed to steal his payment information.",
#     "Lillian sends an email to Andrew, offering financial advice and portfolio management services. The email provides a link to connect with the advisor, but the link leads to a phishing site designed to steal his personal information.",
# ]

# # Create a list of labels (assuming all are fraudulent scenarios)
# labels = ["Fraud"] * len(phishing_scenarios)

# # Create a DataFrame with the phishing scenarios and labels
# df = pd.DataFrame({
#     "scenario": phishing_scenarios,
#     "label": labels
# })

# # Save the DataFrame to a CSV file
# output_csv_path = 'phishing_scenarios.csv'  # Update with your desired file path
# df.to_csv(output_csv_path, index=False)  # Save to CSV without row index



# import pandas as pd

# # List of SIM swap scenarios
# sim_swap_scenarios = [
#     "A scammer uses social engineering to gather information about John through social media and other public sources. They use this information to impersonate him and request a SIM swap from his mobile service provider, gaining control of his phone number.",
#     "A scammer bribes an insider at the mobile service provider to initiate a SIM swap without proper verification, allowing them to take control of Emily's phone number.",
#     "A scammer sends a phishing email to Chris, appearing to be from his mobile service provider. The email asks him to click on a link to verify his account information, leading to a phishing site that captures his details for a SIM swap.",
#     "A scammer intercepts mail intended for Jennifer, containing her replacement SIM card from her mobile service provider. They use the stolen SIM card to take control of her phone number and access her accounts.",
#     "A scammer uses forged documents to impersonate Mark and request a SIM swap from his mobile service provider. This allows the scammer to gain control of his phone number and receive authentication codes intended for him.",
#     "A scammer contacts Olivia with a fake survey, asking for her personal information, including her mobile number and other account details. The scammer then uses this information to request a SIM swap from her mobile service provider.",
#     "A scammer sends a phishing text message to Ethan, claiming to be from his mobile service provider. The text requests that he click on a link to update his account information, leading to a phishing site that captures his details for a SIM swap.",
#     "A scammer convinces an insider at a mobile service provider to swap Jack's SIM card with a new one controlled by the scammer, allowing them to take control of his phone number.",
#     "A scammer hacks into Sarah's online account with her mobile service provider and initiates a SIM swap without her knowledge, giving them control of her phone number and authentication codes.",
#     "A scammer bribes staff at a mobile service provider's retail store to initiate a SIM swap without proper verification, allowing them to take control of David's phone number.",
#     "A scammer calls Lily, pretending to be from her mobile service provider. They ask for her account information to verify her identity, but it's a scam to gather details for a SIM swap.",
#     "A scammer creates a fake website that appears to be from a mobile service provider. They lure Henry to the site through a phishing email or text message, where they capture his account information to initiate a SIM swap.",
#     "A scammer steals Lucas's phone and uses it to request a SIM swap from his mobile service provider, allowing them to gain control of his phone number.",
#     "A scammer calls Lucy, pretending to be a technical support agent from her mobile service provider. They ask for her account information to resolve a technical issue, but it's a scam to gather information for a SIM swap.",
#     "A scammer sends a phishing email to George, claiming there's an issue with his account and asking him to verify his information. The scammer uses the captured information to request a SIM swap from his mobile service provider.",
#     "A scammer uses forged identification to impersonate Monica at her mobile service provider's retail store, allowing them to request a SIM swap and gain control of her phone number.",
#     "A scammer hacks into Isabella's account with her mobile service provider and initiates a SIM swap without her knowledge, allowing them to take control of her phone number and intercept authentication codes.",
#     "A scammer gains unauthorized access to the internal systems of a mobile service provider and initiates a SIM swap for Andrew, gaining control of his phone number without his consent.",
#     "A scammer sends a phishing email to Jenna, claiming she's won a prize and asking her to click on a link to claim it. The link leads to a phishing site designed to gather information for a SIM swap.",
#     "A scammer steals Emma's SIM card from her phone and uses it to request a SIM swap from her mobile service provider, gaining control of her phone number and receiving authentication codes.",
#     "A scammer bribes call center staff at a mobile service provider to initiate a SIM swap without proper verification, allowing them to take control of Ethan's phone number.",
#     "A scammer sends a phishing text message to Ava, claiming there's an issue with her account and asking her to click on a link to resolve it. The link leads to a phishing site designed to capture her account information for a SIM swap.",
#     "A scammer convinces an insider with access to customer data at a mobile service provider to initiate a SIM swap for Alice, allowing them to take control of her phone number without her knowledge.",
#     "A scammer creates a fake website that appears to be from a mobile service provider. They send Bruce a phishing email or text message, claiming there's a security update and asking him to visit the site, leading to a phishing site designed to capture his account information for a SIM swap.",
#     "A scammer hacks into Anthony's online account with his mobile service provider and initiates a SIM swap, allowing them to take control of his phone number without his consent.",
#     "A scammer acquires customer data from an insider at a mobile service provider and uses it to initiate a SIM swap for Veronica, gaining control of her phone number without her knowledge.",
#     "A scammer steals Robert's personal documents, including his driver's license, and uses them to request a SIM swap at his mobile service provider's retail store, allowing them to gain control of his phone number.",
#     "A scammer calls Tom, pretending to be from his mobile service provider's customer service department. They ask for his account information to resolve a supposed technical issue, but it's a scam to gather information for a SIM swap.",
#     "A scammer sends a phishing email to Helen, claiming there's a technical issue with her mobile service and asking her to click on a link to fix it. The link leads to a phishing site designed to capture her account information for a SIM swap.",
#     "A scammer harvests personal data from John's social media accounts to gather enough information to request a SIM swap at his mobile service provider's retail store, allowing them to gain control of his phone number without his consent."
# ]

# # Create a list of labels (assuming all are fraudulent scenarios)
# labels = ["Fraud"] * len(sim_swap_scenarios)

# # Create a DataFrame with the SIM swap scenarios and labels
# df = pd.DataFrame({
#     "scenario": sim_swap_scenarios,
#     "label": labels
# })

# # Save the DataFrame to a CSV file
# output_csv_path = 'sim_swap_scenarios.csv'  # Update with your desired file path
# df.to_csv(output_csv_path, index=False)  # Save to CSV without row index



# import pandas as pd

# # New vishing (phone call scam) scenarios
# vishing_scenarios = [
#     "Alice receives a call from 'Sam' claiming to be from her bank's fraud department. He says that there's suspicious activity on her account and asks her to confirm her account number and the one-time password (OTP) sent to her phone.",
#     "Ben gets a call from 'Lily' from the customer service team at XYZ Bank. Lily mentions that there's an issue with his account and requests his credit card number and CVV to resolve the problem.",
#     "Clara receives a call from 'Mike' who claims to be from the local utility company. He threatens to cut off her electricity unless she provides her bank details to pay the outstanding bill.",
#     "David answers an automated call informing him that his bank account has been locked due to suspicious activity. He's instructed to press '1' to speak with a customer service agent, who asks for personal information to unlock the account.",
#     "Emma receives a call from 'John' claiming to be conducting a survey on behalf of ABC Bank. He asks her for her bank account details, suggesting it's for research purposes.",
#     "Frank gets a call from 'Jessica' who claims to be from a government agency offering financial assistance due to the pandemic. Jessica asks for his bank details to process the payment.",
#     "Grace receives a call from 'Tom' claiming to be from her bank, stating that her account will be closed unless she provides her login credentials for verification.",
#     "Henry gets a call from 'Linda' claiming to represent a charity organization. Linda asks for a donation and requests Henry's bank details to process the payment.",
#     "Irene is called by 'Oscar' who claims that she's won a prize in a contest. Oscar asks for her bank account details to verify her identity and claim the prize.",
#     "Jack receives a call from 'Rachel' pretending to be a law enforcement officer. She threatens legal action for non-payment of a fictitious debt and requests immediate payment, asking for his banking information to settle the alleged debt."
# ]

# # Create labels for the new scenarios
# vishing_labels = ["Fraud"] * len(vishing_scenarios)

# # Read the existing CSV file
# existing_csv_path = 'fraud_scenarios.csv'  # Path to your existing CSV file
# df_existing = pd.read_csv(existing_csv_path)  # Read the existing data

# # Create a DataFrame with the new scenarios and labels
# df_new = pd.DataFrame({
#     "scenario": vishing_scenarios,
#     "label": vishing_labels
# })

# # Concatenate the new DataFrame with the existing one
# df_combined = pd.concat([df_existing, df_new], ignore_index=True)

# # Save the combined DataFrame back to the CSV file
# df_combined.to_csv(existing_csv_path, index=False)  # Save without row index


# import pandas as pd

# # New phishing (email scam) scenarios
# phishing_scenarios = [
#     "Alice receives an email that looks like it's from her bank, stating that her account has been suspended. The email urges her to click on a link to restore access. The link leads to a phishing website.",
#     "Ben gets an email that appears to be from a popular online retailer, stating that he's eligible for a refund on a recent purchase. The email includes a link to claim the refund, but it leads to a phishing site.",
#     "Clara receives an email that looks like it's from her favorite social media platform. The email claims there's been suspicious activity on her account and provides a link to reset her password. The link leads to a phishing site.",
#     "David receives an email appearing to be from a shipping company, stating that a package couldn't be delivered. The email includes a link to reschedule the delivery, but it leads to a phishing site.",
#     "Emma receives an email that seems to be from a reputable company, offering her a job. The email asks for her banking information for payroll setup, but it's a phishing attempt.",
#     "Frank receives an email appearing to be from his bank. The email asks him to update his account information by clicking on a link. The link directs him to a phishing website designed to steal his credentials.",
#     "Grace gets an email claiming to be from a government agency, stating that she's eligible for a tax refund. The email includes a link to submit her banking details for processing, but it's a phishing site.",
#     "Henry receives an email pretending to be from a popular streaming service. The email says there's a billing issue and asks him to update his payment information by clicking on a link, leading to a phishing page.",
#     "Irene receives an email that appears to be a software update notification. The email prompts her to download an attachment to update her software, but the attachment contains malware designed to steal her banking credentials.",
#     "Jack receives an email claiming that he's won a lottery prize. The email asks him to provide his banking information to claim the prize, but it's a phishing attempt."
# ]

# # Create labels for the new scenarios
# phishing_labels = ["Fraud"] * len(phishing_scenarios)

# # Read the existing CSV file
# existing_csv_path = 'phishing_scenarios.csv'  # Path to your existing CSV file
# df_existing = pd.read_csv(existing_csv_path)  # Read the existing data

# # Create a DataFrame with the new scenarios and labels
# df_new = pd.DataFrame({
#     "scenario": phishing_scenarios,
#     "label": phishing_labels
# })

# # Concatenate the new DataFrame with the existing one
# df_combined = pd.concat([df_existing, df_new], ignore_index=True)

# # Save the combined DataFrame back to the CSV file
# df_combined.to_csv(existing_csv_path, index=False)  # Save without row index

# import pandas as pd

# # New SIM Swap (Mobile Number Scam) scenarios
# sim_swap_scenarios = [
#     "Alice's phone suddenly loses service. When she contacts her mobile service provider, she finds out that her SIM card was replaced by someone who pretended to be her, gaining control of her phone number and access to her online accounts.",
#     "Ben receives an email that seems to be from his mobile service provider, stating that his SIM card needs to be replaced due to a technical upgrade. The email includes a link to confirm his identity, which leads to a phishing site asking for his personal information.",
#     "Clara finds out that her SIM card was replaced after an insider at her mobile service provider was bribed to perform the swap. This allowed scammers to take control of her phone number and access her online accounts through two-factor authentication (2FA).",
#     "David's SIM card is swapped by scammers who had gathered his personal information from various sources. They used this information to convince his mobile service provider to issue a new SIM card in their favor, gaining control of his phone number.",
#     "Emma receives a call from someone pretending to be from her mobile service provider. The caller claims that her SIM card needs to be replaced and asks for her account details to complete the process. The information is then used to initiate a SIM swap.",
#     "Frank's mobile service provider receives a request to replace his SIM card, along with forged documents. The scammers used this method to gain control of his phone number, allowing them to intercept his two-factor authentication codes and access his online accounts.",
#     "Grace's social media account is hacked, allowing the scammers to collect enough personal information to request a SIM swap. They use this access to attempt unauthorized transactions on her bank account.",
#     "Henry visits a phishing website that mimics his mobile service provider's login page. After entering his credentials, scammers use this information to request a SIM swap, gaining control of his phone number and disrupting his online accounts.",
#     "Irene discovers that her SIM card was swapped after a scammer bribed an employee at her mobile service provider. This insider collusion allowed the scammers to take control of her phone number and attempt fraudulent activities with her online accounts.",
#     "Jack's mobile service provider sent him a replacement SIM card, but it was intercepted and stolen by scammers. They then used the new SIM card to gain control of his phone number, potentially compromising his online accounts."
# ]

# # Create labels for the new scenarios
# sim_swap_labels = ["Fraud"] * len(sim_swap_scenarios)

# # Read the existing CSV file
# existing_csv_path = 'sim_swap_scenarios.csv'  # Path to your existing CSV file
# df_existing = pd.read_csv(existing_csv_path)  # Read the existing data

# # Create a DataFrame with the new scenarios and labels
# df_new = pd.DataFrame({
#     "scenario": sim_swap_scenarios,
#     "label": sim_swap_labels
# })

# # Concatenate the new DataFrame with the existing one
# df_combined = pd.concat([df_existing, df_new], ignore_index=True)

# # Save the combined DataFrame back to the CSV file
# df_combined.to_csv(existing_csv_path, index=False)  # Save without row index


# import pandas as pd

# # New vishing scenarios to add to the CSV
# vishing_scenarios = [
#     "A caller claims to be from your bank's fraud department and informs you that your account has been compromised. They request your account number, password, and OTP to verify your identity.",
#     "Someone posing as a bank representative calls you, stating that there's an issue with your account and asks for your card details and CVV for verification.",
#     "An automated voice message informs you that your account has been locked due to suspicious activity and prompts you to press a number to speak with a customer service agent, who then asks for your personal information.",
#     "A caller pretends to be conducting a survey on behalf of your bank and asks for your account details, claiming it's for research purposes.",
#     "You receive a call claiming to be from a government agency offering financial assistance due to the pandemic, but they require your bank details to process the payment.",
#     "A scammer poses as a bank employee and tells you that your account is about to be closed unless you provide your login credentials for verification.",
#     "A caller says they are updating their records and need you to confirm your account information, including your address, phone number, and security questions.",
#     "Someone pretending to be a bank representative informs you that your account has been selected for a special offer but requires your personal and financial information to proceed.",
#     "You receive a call congratulating you on winning a prize but need to verify your identity by providing your bank account details.",
#     "A caller threatens legal action against you for non-payment of a fictitious debt and demands immediate payment, requesting your banking information to process the transaction.",
#     "A recorded message claims to be from your bank and asks you to press a button to verify your account, leading you to a live agent who requests sensitive information.",
#     "A scammer poses as a tech support agent from a well-known company and asks for your bank account details to process a refund for a supposed overcharge.",
#     "You receive a call offering a lower interest rate on your credit card but require your card number and expiry date for verification.",
#     "A caller claims to be from a charity organization and requests a donation, but they need your bank details to process the transaction.",
#     "An automated message informs you of a security breach on your account and requests your personal information to secure your account.",
#     "Someone claiming to be a bank representative offers a pre-approved loan but requires your personal information to finalize the application.",
#     "A caller impersonates a law enforcement officer and threatens arrest for unpaid taxes unless immediate payment is made, asking for your banking information to settle the alleged debt.",
#     "You receive a call stating that your account has been credited with a refund but needs your banking information to confirm the transaction.",
#     "A recorded message informs you of suspicious activity on your account and prompts you to speak with a representative by pressing a button, leading to a scammer who requests your sensitive information.",
#     "A caller poses as a utility provider and threatens to disconnect your services unless an outstanding bill is paid immediately, requesting your banking details for payment."
# ]

# # Create labels for the new scenarios
# labels = ["Fraud"] * len(vishing_scenarios)

# # Path to your existing CSV file
# existing_csv_path = 'fraud_scenarios.csv' 

# # Read the existing CSV file
# df_existing = pd.read_csv(existing_csv_path)  

# # Create a DataFrame with the new scenarios and labels
# df_new = pd.DataFrame({
#     "scenario": vishing_scenarios,
#     "label": labels
# })

# # Concatenate the new DataFrame with the existing one
# df_combined = pd.concat([df_existing, df_new], ignore_index=True)

# # Save the combined DataFrame back to the CSV file
# df_combined.to_csv(existing_csv_path, index=False)  # Save without row index


# import pandas as pd

# # New phishing scenarios to add to the CSV
# phishing_scenarios = [
#     "You receive an email claiming to be from your bank, stating that your account has been suspended and urging you to click on a link to restore access.",
#     "An email supposedly from a popular online retailer informs you of a refund for a recent purchase and includes a link to claim the refund, leading to a phishing website.",
#     "A fraudulent email mimicking a social media platform notifies you of suspicious activity on your account and prompts you to click on a link to verify your identity.",
#     "You receive an email appearing to be from a shipping company, stating that a package couldn't be delivered and requesting you to click on a link to reschedule delivery, leading to a phishing site.",
#     "An email disguised as a job offer from a reputable company requires you to provide your banking information for payroll setup, but it's actually a phishing attempt.",
#     "An email pretending to be from a financial institution asks you to update your account information by clicking on a link, directing you to a fake website designed to steal your credentials.",
#     "You receive an email posing as a government agency, claiming that you're eligible for a tax refund and providing a link to submit your banking details for processing.",
#     "An email impersonating a popular streaming service informs you of a billing issue and requests you to update your payment information by clicking on a link, leading to a phishing page.",
#     "A fraudulent email disguised as a software update notification prompts you to download an attachment containing malware, which can steal your banking credentials.",
#     "An email pretending to be from a charity organization solicits donations and includes a link to donate, but it leads to a fake website designed to steal your payment information.",
#     "You receive an email claiming to be from a lottery organization, stating that you've won a prize and need to provide your banking information to claim it.",
#     "An email appearing to be from a travel agency offers exclusive deals on vacation packages and requires you to enter your credit card details on a linked website, which is a phishing site.",
#     "A fraudulent email posing as a software license renewal notice prompts you to click on a link to renew your subscription and enter your payment details, leading to a phishing page.",
#     "An email pretending to be from a package delivery service notifies you of an attempted delivery and asks you to confirm your identity by providing your banking information to reschedule delivery.",
#     "You receive an email claiming to be from a financial advisor, offering investment opportunities and requiring your banking details to proceed with transactions, but it's a phishing attempt.",
#     "An email disguised as a password reset request from a popular social media platform prompts you to click on a link to reset your password, leading to a phishing site.",
#     "A fraudulent email impersonating a tech support team informs you of a security breach on your account and requests you to verify your identity by providing your banking information.",
#     "An email posing as a customer satisfaction survey from a reputable company asks you to click on a link to participate and provide your banking details for a chance to win a prize, but it's a phishing scam.",
#     "You receive an email appearing to be from a job recruitment agency, asking you to provide your banking information for a background check, but it's actually a phishing attempt.",
#     "An email pretending to be from a health insurance provider informs you of a refund due to overpayment and asks you to click on a link to claim the refund, leading to a phishing website."
# ]

# # Create labels for the new scenarios
# labels = ["Phishing"] * len(phishing_scenarios)

# # Path to your existing CSV file
# existing_csv_path = 'phishing_scenarios.csv'

# # Read the existing CSV file
# df_existing = pd.read_csv(existing_csv_path)

# # Create a DataFrame with the new scenarios and labels
# df_new = pd.DataFrame({
#     "scenario": phishing_scenarios,
#     "label": labels
# })

# # Concatenate the new DataFrame with the existing one
# df_combined = pd.concat([df_existing, df_new], ignore_index=True)

# # Save the combined DataFrame back to the CSV file
# df_combined.to_csv(existing_csv_path, index=False)  # Save without row index


# import pandas as pd

# # New SIM swap scenarios to add to the CSV
# sim_swap_scenarios = [
#     "A scammer contacts your mobile service provider posing as you and convinces them to deactivate your current SIM card and activate a new one under their control.",
#     "Fraudsters gather personal information about you from social media or other sources and use it to impersonate you when requesting a SIM card replacement from your mobile service provider.",
#     "A hacker gains access to your mobile service provider's systems and initiates a SIM swap without your knowledge or consent.",
#     "Scammers deceive you into providing sensitive information over the phone, claiming to be conducting a survey or offering a prize, and then use that information to request a SIM swap.",
#     "A fraudulent website tricks you into entering your mobile number and other personal details, which are then used to request a SIM card replacement from your mobile service provider.",
#     "A scammer steals your identity and uses forged documents to request a SIM card replacement from your mobile service provider, claiming that your phone was lost or stolen.",
#     "You receive a phishing email or text message that appears to be from your mobile service provider, asking you to click on a link to verify your account information, leading to a SIM swap.",
#     "A scammer bribes an insider at your mobile service provider to initiate a SIM swap without proper authorization or verification.",
#     "Fraudsters intercept your mail and steal the SIM card replacement sent by your mobile service provider, allowing them to take control of your phone number.",
#     "A malicious app installed on your phone collects information about you, including your mobile number and account details, which are then used to request a SIM swap."
# ]

# # Create labels for the new scenarios
# labels = ["SIM Swap"] * len(sim_swap_scenarios)

# # Path to your existing CSV file
# existing_csv_path = 'sim_swap_scenarios.csv'

# # Read the existing CSV file
# df_existing = pd.read_csv(existing_csv_path)

# # Create a DataFrame with the new scenarios and labels
# df_new = pd.DataFrame({
#     "scenario": sim_swap_scenarios,
#     "label": labels
# })

# # Concatenate the new DataFrame with the existing one
# df_combined = pd.concat([df_existing, df_new], ignore_index=True)

# # Save the combined DataFrame back to the CSV file
# df_combined.to_csv(existing_csv_path, index=False)  # Save without row index

# import pandas as pd

# # List of website spoofing scenarios
# website_spoofing_scenarios = [
#     "Bank Spoofing Site: A fake website that mimics a major bank's homepage, designed to steal login credentials.",
#     "E-commerce Spoofing Site: A spoofed version of a popular online retailer's website, used to capture credit card information.",
#     "Government Agency Spoofing Site: A fraudulent website posing as a government agency, designed to collect sensitive personal data.",
#     "Social Media Platform Spoofing Site: A fake social media login page used to capture usernames and passwords.",
#     "Email Provider Spoofing Site: A spoofed email provider's login page used to steal email account credentials.",
#     "Streaming Service Spoofing Site: A fake streaming service website designed to obtain payment information.",
#     "Software Update Spoofing Site: A spoofed website claiming to offer software updates, but distributing malware.",
#     "Technical Support Spoofing Site: A fraudulent technical support site used to gather personal information and payment details.",
#     "Online Banking Spoofing Site: A fake online banking website that captures user login details and OTPs.",
#     "Charity Organization Spoofing Site: A spoofed charity donation site designed to steal credit card information.",
#     "Telecommunications Company Spoofing Site: A fake telecommunications website used to initiate SIM swaps and steal personal information.",
#     "Online Auction Spoofing Site: A spoofed online auction site that deceives users into providing payment information.",
#     "Shipping Company Spoofing Site: A fake website posing as a shipping company, designed to collect tracking information and other personal details.",
#     "Job Recruitment Spoofing Site: A fraudulent website posing as a job recruitment site, designed to gather personal information and bank details.",
#     "Utility Provider Spoofing Site: A spoofed website that pretends to be a utility provider, aiming to steal payment information.",
#     "Tax Refund Spoofing Site: A fake website claiming to process tax refunds, used to gather personal and financial information.",
#     "Online Gaming Spoofing Site: A spoofed online gaming platform used to steal account credentials and payment information.",
#     "Pharmacy Spoofing Site: A fraudulent website pretending to be an online pharmacy, used to capture personal and payment information.",
#     "Travel Agency Spoofing Site: A fake travel agency site designed to steal credit card information and personal data.",
#     "Fitness App Spoofing Site: A spoofed fitness app website that captures login credentials and payment information.",
#     "Educational Institution Spoofing Site: A fake website pretending to be an educational institution, designed to gather personal and financial data.",
#     "Hotel Reservation Spoofing Site: A fraudulent website posing as a hotel reservation site, aiming to steal payment information.",
#     "Non-Profit Organization Spoofing Site: A spoofed non-profit organization's website, used to capture personal and financial data.",
#     "Electronics Store Spoofing Site: A fake electronics store website used to obtain credit card information.",
#     "Sports Team Spoofing Site: A spoofed sports team website designed to gather personal and financial information.",
#     "Online Magazine Spoofing Site: A fake online magazine website that distributes malware.",
#     "Video Game Store Spoofing Site: A spoofed video game store website used to capture credit card information.",
#     "Real Estate Agency Spoofing Site: A fraudulent website posing as a real estate agency, designed to collect personal and financial data.",
#     "Health Clinic Spoofing Site: A fake website pretending to be a health clinic, aiming to steal personal information.",
#     "Musical Band Spoofing Site: A spoofed musical band's website designed to capture personal information and distribute malware.",
#     "News Outlet Spoofing Site: A fake news website that redirects users to phishing or malware-laden sites.",
#     "Political Campaign Spoofing Site: A spoofed political campaign website used to gather personal and financial data.",
#     "Local Government Spoofing Site: A fraudulent website pretending to be a local government office, designed to gather personal and financial information.",
#     "Sports Event Spoofing Site: A fake sports event website aiming to steal credit card information.",
#     "Software License Renewal Spoofing Site: A spoofed software license renewal website used to gather payment information.",
#     "Insurance Company Spoofing Site: A fake insurance company's website aiming to capture personal and financial information.",
#     "Job Application Spoofing Site: A spoofed job application website that gathers personal information and bank details.",
#     "Internet Service Provider Spoofing Site: A fake internet service provider website used to initiate SIM swaps and steal personal information.",
#     "Investment Firm Spoofing Site: A fraudulent website posing as an investment firm, designed to gather personal and financial data.",
#     "Beauty Product Spoofing Site: A spoofed beauty product website that aims to capture payment information.",
#     "Home Improvement Store Spoofing Site: A fake home improvement store website used to gather credit card information.",
#     "Non-Profit Fundraiser Spoofing Site: A spoofed non-profit fundraiser website designed to steal personal and financial data.",
#     "Property Rental Spoofing Site: A fake property rental website aiming to capture personal and financial information.",
#     "Software Company Spoofing Site: A fraudulent website pretending to be a software company, designed to gather personal and financial data.",
#     "Television Channel Spoofing Site: A fake television channel's website that distributes malware.",
#     "Cosmetic Store Spoofing Site: A spoofed cosmetic store website aiming to capture credit card information.",
#     "DIY Store Spoofing Site: A fraudulent website posing as a DIY store, used to gather personal and financial data.",
#     "Food Delivery Service Spoofing Site: A fake food delivery service website used to gather credit card information.",
#     "Real Estate Listing Spoofing Site: A spoofed real estate listing website designed to steal personal and financial information.",
#     "Computer Hardware Store Spoofing Site: A fraudulent website posing as a computer hardware store, used to gather personal and financial data."
# ]

# # Create a DataFrame with the scenarios
# df = pd.DataFrame({
#     "scenario": website_spoofing_scenarios,
#     "label": ["Website Spoofing"] * 50  # Adding labels for each scenario
# })

# # Save the DataFrame to a CSV file
# df.to_csv("website_spoofing_scenarios.csv", index=False)  # Save without row index
import pandas as pd

# List of safe scenarios as strings
safe_scenarios = [
    "I received an email from my bank confirming my recent transaction.",
    "A call from my insurance company reminded me about my policy renewal.",
    "I visited my bank's official website to check my balance.",
    "My phone provider sent me an email about upcoming maintenance.",
    "I received a text message from my doctor's office confirming my appointment.",
    "I signed into my bank account online to check my statement.",
    "A friend sent me an email with a link to a news article.",
    "I received a call from my phone carrier about a network upgrade.",
    "My bank sent me a text message confirming my recent withdrawal.",
    "I received a reminder email from my gym about my membership renewal.",
    "I got a text message from my dentist confirming my appointment.",
    "My ISP sent me an email about planned service maintenance.",
    "I received a call from a delivery service about my package's arrival.",
    "I logged into my work email to check for updates on a project.",
    "My insurance company sent me an email with policy updates.",
    "I received an email about an upcoming software update for my phone.",
    "I got a text message from my car dealership about my next service.",
    "My credit card company sent me an email confirming my recent purchase.",
    "I received an email with a receipt for an online purchase I made.",
    "My energy company sent me an email with my monthly bill.",
    "I got a call from my landlord about upcoming building maintenance.",
    "My streaming service sent me an email with new content recommendations.",
    "I received a text message from my cable provider about a new channel.",
    "I got an email from my travel agent confirming my flight details.",
    "My doctor's office sent me an email with my test results.",
    "I got a text message from my bank with a one-time code for login.",
    "My phone provider sent me a text message about a new plan.",
    "I received an email from my credit card company with my monthly statement.",
    "I got a call from my optometrist about my next eye exam.",
    "My bank sent me a text message confirming a change in my account settings.",
    "I received an email from my utility company with a payment reminder.",
    "My ISP sent me a text message with information on new services.",
    "I received an email about an upcoming community event.",
    "I got a text message from my hairdresser about my appointment.",
    "My airline sent me an email confirming my flight reservation.",
    "I received a call from my pet groomer about my dog's next appointment.",
    "I got an email from my accountant with tax preparation tips.",
    "My water utility company sent me an email with a payment reminder.",
    "I got a text message from my phone provider about a new app.",
    "I received an email from my music streaming service with a playlist recommendation.",
    "My mobile carrier sent me a text message about a new data plan.",
    "I received an email from my landlord about upcoming renovations.",
    "I got a call from my mortgage company about a new loan offer.",
    "My bank sent me an email with tips on avoiding fraud.",
    "I received a text message from my doctor's office with a health tip.",
    "I got an email from my ISP about my data usage for the month.",
    "My phone provider sent me a text message about a security update.",
    "I received an email from my fitness app with a new workout plan.",
    "My insurance company sent me an email with policy renewal information.",
    "I got a text message from my power company about a planned outage.",
    "I received an email from my real estate agent with new property listings.",
    "My car insurance company sent me an email about my policy renewal.",
    "I got a call from my cable provider about a new package offer.",
    "I received a text message from my gym about a new class.",
    "My bank sent me an email with tips for managing my finances.",
    "I received an email from my mobile carrier with a discount code.",
    "My credit card company sent me a text message with a security alert.",
    "I got a call from my water utility company about an upcoming maintenance.",
    "My landlord sent me a text message about an inspection.",
    "I received an email from my cable provider about a new show.",
    "My travel agent sent me a text message confirming my hotel booking.",
    "I got a call from my pet sitter about my next booking.",
    "I received an email from my insurance company with a claim update.",
    "My bank sent me a text message about a new online feature.",
    "I got a text message from my doctor about my upcoming check-up.",
    "My phone provider sent me a text message about a new service.",
    "I received an email from my utility company with energy-saving tips.",
    "My credit card company sent me a text message with a fraud alert.",
    "I got an email from my cable provider with new movie recommendations.",
    "I received a call from my auto insurance company about a policy review.",
    "My bank sent me an email about online security.",
    "I received a text message from my bank confirming a deposit.",
    "I got an email from my travel agent with a special vacation offer.",
    "My ISP sent me a text message with new internet speeds.",
    "I received an email from my health insurance company with a wellness tip.",
    "My phone provider sent me a text message about a new loyalty program.",
    "My cable provider sent me an email about a new feature.",
    "I received an email from my mortgage company about a payment update.",
    "I got a text message from my car insurance company about a policy renewal.",
    "My ISP sent me a text message about an upcoming service interruption.",
    "I received an email from my bank with updates on their services.",
    "My streaming service sent me a text message with a new movie release.",
    "I got a call from my water utility company about my monthly bill.",
    "I received an email from my ISP about my internet usage.",
    "My bank sent me a text message with a security reminder.",
    "I got an email from my insurance company with a new coverage offer.",
    "My power company sent me a call about a planned power outage.",
    "My ISP sent me an email with a reminder to update my account information.",
    "I got a call from my mortgage company about refinancing options.",
    "I received a text message from my bank about a new feature for online banking.",
    "My health insurance provider sent me an email with a wellness tip.",
    "My power company sent me a call about a planned power outage.",
    "My bank sent me an email about online security.",
    "I received a text message from my power company with a planned power outage reminder.",
    "My ISP sent me an email about planned network maintenance."
]

# Create a DataFrame with the safe scenarios
df = pd.DataFrame({
    "scenario": safe_scenarios,
    "label": ["Safe"] * len(safe_scenarios)  # Adding a label for each scenario
})

# Save the DataFrame to a CSV file
df.to_csv("safe_scenarios.csv", index=False)  # Save without row index
