import json
import os
from transformers import BertTokenizer


def preprocess():
    data_key = ['test', 'train', 'val']
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(base_dir, './data')
    pro_dir = os.path.join(base_dir, './data/pro_data')
    if not os.path.exists(pro_dir):
        os.makedirs(pro_dir)
    data = {}
    for key in data_key:
        data[key] = json.load(os.path.join(data_dir, '{}.json'.format(key)))
    pro_data = {}
    all_intent = []
    all_tag = []
    tokenizer = BertTokenizer.from_pretrained('hfl/chinese-bert-wwm-ext')
    for key in data_key:
        pro_data[key] = []
        for no, sess in data[key].items():
            context = []
            for i, turn in enumerate(sess['messages']):
                utterance = turn['content']
                tokens = tokenizer.tokenize(utterance)
                golden = []
                span_info = []
                intents = []
                for intent, domain, slot, value in turn['dialog_act']:

