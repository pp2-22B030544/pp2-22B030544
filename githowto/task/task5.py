questions = [
    {
        'question' : 'which command  we use when used number ? ', 
        'answer' : [
            '0. int',
            '1. str',
            '2. float',
        ],
        'correct_ans' : 1   },
        {'question' : 'which command  we use when used string ? ', 
        'answer' : [
            '0. int',
            '2. str',
            '1. float',
        ],
        'correct_ans' : 2 

        }
]

corect_ans_cnt =0
for question in questions :
    print(question['question'])
    for answer in question :
        print(question['answer'])

