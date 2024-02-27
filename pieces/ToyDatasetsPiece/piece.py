from sklearn.datasets import load_iris, load_diabetes, load_digits, load_wine, load_breast_cancer
import pandas as pd
from domino.base_piece import BasePiece
from .models import InputModel, OutputModel
from pathlib import Path

class ToyDatasetsPiece(BasePiece):

    def piece_function(self, input_data: InputModel):
        dataset_name = input_data.dataset
        if dataset_name == 'iris':
            dataset = load_iris()
        elif dataset_name == 'diabetes':
            dataset = load_diabetes()
        elif dataset_name == 'digits':
            dataset = load_digits()
        elif dataset_name == 'wine':
            dataset = load_wine()
        elif dataset_name == 'breast_cancer':
            dataset = load_breast_cancer()
        else:
            raise ValueError(f'Unknown dataset name: {dataset_name}')

        df = pd.DataFrame(dataset.data, columns=dataset.feature_names)
        df['target'] = dataset.target

        file_path = str(Path(self.results_path) / f'{dataset_name}.csv')
        df.to_csv(file_path, index=False)

        return OutputModel(
            file_path=file_path
        )
