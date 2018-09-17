import os
from flask import current_app, g
from model import Model

def get_model(model_path, embedding_path):
    if 'model' not in g:
        g.model = Model(model_path=model_path)
        g.model.parameters['pre_emb'] = os.path.join(os.getcwd(), embedding_path)
        g.inference = g.model.build(training=False, **g.model.parameters)
        g.model.reload()

    return g.model, g.inference
