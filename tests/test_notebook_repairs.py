"""Run notebook code on small offline data; preserve archived outputs."""
import ast
import json
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pytest
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

ROOT=Path(__file__).resolve().parents[1]/'python_machine_learning'


def source(name,index):
    return ''.join(json.loads((ROOT/name).read_text(encoding='utf-8'))['cells'][index-1]['source'])


@pytest.mark.parametrize('name',['Gradient_Descent.ipynb','Gradient_Descent(경사하강).ipynb'])
def test_gradient_matches_finite_differences_and_apis_survive_later_definitions(name):
    ns={'np':np};nodes=[]
    for c in json.loads((ROOT/name).read_text(encoding='utf-8'))['cells']:
        if c['cell_type']=='code':nodes += [n for n in ast.parse(''.join(c['source'])).body if isinstance(n,ast.FunctionDef)]
    exec(compile(ast.Module(nodes,type_ignores=[]),name,'exec'),ns)
    x=np.linspace(0,1,25);y=3*x+2;w,b=1.,0.5
    dw,db=ns['Gradient'](x,y,w,b)
    loss=lambda w,b: np.mean((y-(w*x+b))**2)
    h=1e-6
    np.testing.assert_allclose([dw,db],[(loss(w+h,b)-loss(w-h,b))/(2*h),(loss(w,b+h)-loss(w,b-h))/(2*h)],atol=1e-8)
    assert len(ns['Learning'](x,y,w,b,0.01))==2
    assert len(ns['Learning_with_loss'](x,y,w,b,0.01))==3
    for _ in range(3000):w,b=ns['Learning'](x,y,w,b,0.05)
    np.testing.assert_allclose([w,b],[3,2],atol=1e-7)


def test_decision_tree_offline_execution_and_class_labels():
    name='Decision_Tree.ipynb';ns={}
    for i in [3,8,9,10,11,12,13]:
        ns['plt']=plt
        exec(source(name,i),ns)
    assert ns['Model_dt'].classes_.tolist()==['setosa','versicolor','virginica']
    assert len(ns['y_test'])==45
    assert (ns['y_hat']==ns['y_test']).mean()>0.8
    plt.close('all')


def test_completed_random_forest_runs_without_downloads():
    ns={};exec(source('Random_Forest.ipynb',1),ns)
    assert ns['model'].n_estimators==200
    assert len(ns['y_test'])==45
    assert ns['importance'].sum()==pytest.approx(1)
    assert (ns['predicted']==ns['y_test']).mean()>0.8


def test_bike_actual_ols_cells_use_series_target():
    import statsmodels.formula.api as smf
    rng=np.random.default_rng(42);n=120
    data=pd.DataFrame({name:rng.uniform(0,10,n) for name in ['temp','humidity','windspeed','month','hour']})
    data['holiday']=rng.integers(0,2,n);data['workingday']=rng.integers(0,2,n)
    data['count']=10+2*data.temp+3*data.hour+rng.normal(size=n)
    train,test=train_test_split(data,test_size=0.3,random_state=2045)
    ns={'smf':smf,'np':np,'train_set':train,'test_set':test,'mean_squared_error':mean_squared_error}
    name='Mini_project_Kaggle_Bike_Sharing_Demand_Modeling.ipynb'
    for i in [53,54,55,57,58,59]:exec(source(name,i),ns)
    assert np.isfinite(ns['mse1']) and np.isfinite(ns['mse2'])
    expected=np.mean((test['count']-ns['y_hat_1'])**2)
    assert ns['mse1']==pytest.approx(expected)


def test_fraud_plots_use_correct_estimator_and_modern_seaborn():
    from sklearn.tree import DecisionTreeClassifier
    import seaborn as sns
    rng=np.random.default_rng(42)
    X=pd.DataFrame(rng.normal(size=(80,29)))
    y=np.tile([0,0,0,1],20)
    ns={'plt':plt,'sns':sns,'X':X,'Model_dt':DecisionTreeClassifier(random_state=42).fit(X,y),
        'Model_pr':DecisionTreeClassifier(max_depth=5,random_state=42).fit(X,y)}
    name='Mini_project_Kaggle_Fraud_Detection_Modeling.ipynb'
    exec(source(name,36),ns)
    observed=[];real=ns['plot_tree']
    def capture(estimator,**kwargs):
        observed.append(estimator)
        return real(estimator,**kwargs)
    ns['plot_tree']=capture
    for i in [37,44,47,52]:exec(source(name,i),ns)
    assert observed==[ns['Model_dt'],ns['Model_pr']]
    plt.close('all')
