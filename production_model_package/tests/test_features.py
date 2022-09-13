from mosaic_minerals_model.config.core import config
from mosaic_minerals_model.processing.features import LogTransformer


def test_log_variable_transformer(sample_input_data):
    # Given
    transformer = LogTransformer(variables=config.model_config.features,
            reference_variable=config.model_config.numericals_log_vars)    
    assert sample_input_data["susc_std"].iat[0] == 0.0003135805311814

    # When
    subject = transformer.fit_transform(sample_input_data)

    # Then
    assert subject["susc_std"].iat[0] == -3.5036509085607963
