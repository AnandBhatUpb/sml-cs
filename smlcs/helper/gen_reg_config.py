import json


def gen_reg_config():
    regressor_config = dict()
    regressor_config['regressors'] = []
    regressor_config['innercv_folds'] = 10

    rf_grid = {'n_estimators': (1000, 2000),
               'max_features': (50, 75),
               'max_depth': (20, 40),
               'min_samples_split': (2, 100),
               'min_samples_leaf': (1, 10),
               }

    regressor_config['regressors'].append({
        'reg_name': 'rf',
        'reg_parameters': rf_grid
    })

    svr_grid = {
        'C': (1e-4, 1e+2, 'log-uniform'),
        'gamma': (1e-6, 1e+1, 'log-uniform'),
        'degree': (1, 8),  # integer valued parameter
        'kernel': ['linear', 'poly', 'rbf'],  # categorical parameter
        }

    regressor_config['regressors'].append({
        'reg_name': 'svr',
        'reg_parameters': svr_grid
    })

    gb_grid = {
        'learning_rate': (0.1, 0.3),
        'n_estimators': (1000, 2000),
        'min_samples_split': (2, 100),
        'min_samples_leaf': (1, 10),
        'max_features': (4, 13),
        'subsample': (0.6, 1.0),
        'max_depth': (5, 20)
    }

    regressor_config['regressors'].append({
        'reg_name': 'gb',
        'reg_parameters': gb_grid
    })

    with open('../configurations/reg_config.txt', 'w') as outfile:
        json.dump(regressor_config, outfile)


gen_reg_config()
