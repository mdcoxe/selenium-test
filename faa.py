import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

website = 'https://free-faa-exam.kingschools.com/private-pilot'

os.environ['PATH'] += ':/home/michaelc/AES/bk-val/selenium-practice/selenium-driver'
driver = webdriver.Chrome()

driver.get(website)

num_quest_gen_input = driver.find_element(By.XPATH, '//input[@id="QuestionsToGenerate"]')
num_quest_gen_input.clear()
num_quest_gen_input.send_keys("60")

start_button = driver.find_element(By.XPATH, '//input[@value="Start Test"]')
start_button.click()

time.sleep(15)

submit_test = driver.find_element(By.XPATH, '//input[@value="Submit Test"]')
submit_test.click()

corrected_quest = driver.find_elements(By.XPATH, '//div[@class="question-container incorrect"]')

quest = []
correct_answer = []
ans_a = []
ans_b = []
ans_c = []

for question in corrected_quest:
    q = question.find_element(By.XPATH, './p[1]').text
    quest.append(q)
    correct = question.find_element(By.XPATH, './div[@class="answer-choice"]//img[@class="answer-image correct"]/following-sibling::label').text
    correct_answer.append(correct)
    a1 = question.find_element(By.XPATH, './div[1][@class="answer-choice"]/label').text
    ans_a.append(a1)
    a2 = question.find_element(By.XPATH, './div[2][@class="answer-choice"]/label').text
    ans_b.append(a2)
    a3 = question.find_element(By.XPATH, './div[3][@class="answer-choice"]/label').text
    ans_c.append(a3)

driver.quit()

df = pd.DataFrame({'question': quest, 'correct_answer': correct_answer, 'ans_a': ans_a, 'ans_b': ans_b, 'ans_c': ans_c})
df.to_csv('faa_practice_questions.csv', mode='a', index=False)
print(df)

