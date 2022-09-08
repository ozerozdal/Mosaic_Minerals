from feature_engine.selection import DropFeatures
from feature_engine.transformation import LogTransformer
from feature_engine.wrappers import SklearnTransformerWrapper
from sklearn.linear_model import Lasso
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import Binarizer, MinMaxScaler

from regression_model.config.core import config

PreOptuna_Pipe = Pipeline(
    [
 
        ("drop_features", DropFeatures(features_to_drop=[config.model_config.ref_var])),
        # ==== VARIABLE TRANSFORMATION =====
        ("log", LogTransformer(variables=config.model_config.numericals_log_vars)),
        
        ("scaler", MinMaxScaler()),
        (
            "Lasso",
            Lasso(
                alpha=config.model_config.alpha,
                random_state=config.model_config.random_state,
            ),
        ),
    ]
)
