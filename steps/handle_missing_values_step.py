import pandas as pd
import matplotlib.pyplot as plt
from src.handle_missing_values import (
    DropMissingValStrategy,
    FillMissingValStrategy,
    MissingValueHandler,
)
from zenml.client import Client
from zenml import step

@step
def handle_missing_values_step(df: pd.DataFrame, strategy: str = "mean") -> pd.DataFrame:
    """Handles missing values using MissingValueHandler and the specified strategy."""
    missing_values_before = df.isnull().sum()
    if strategy == "drop":
        handler = MissingValueHandler(DropMissingValStrategy(axis=0))
    elif strategy in ["mean", "median", "mode", "constant"]:
        handler = MissingValueHandler(FillMissingValStrategy(method=strategy))
    else:
        raise ValueError(f"Unsupported missing value handling strategy: {strategy}")

    cleaned_df = handler.execute_handle_missing_values(df)
    missing_values_after = cleaned_df.isnull().sum()
    # Create a visualization
    fig, ax = plt.subplots(figsize=(10, 6))
    pd.DataFrame({
        "Before Handling": missing_values_before,
        "After Handling": missing_values_after
    }).plot(kind="bar", ax=ax)
    plt.title("Missing Values Before and After Handling")
    plt.xlabel("Columns")
    plt.ylabel("Count")
    plt.xticks(rotation=90)
    plt.tight_layout()

    # Save the visualization as an artifact
    artifact_path = Client().active_stack.artifact_store.path + "/missing_values_plot.png"
    fig.savefig(artifact_path)
    plt.close(fig)

    print(f"Visualization saved at {artifact_path}")

    return cleaned_df
