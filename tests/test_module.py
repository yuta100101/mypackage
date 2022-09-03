import pandas as pd
from mypackage import myfunc


def test_myfunc():
    df = pd.DataFrame({"col1": [0, 1, 2], "col2": [-1, -2, -3]})

    df_result = myfunc(df)

    df_expected = pd.DataFrame({"col1": [0, 2, 4], "col2": [-2, -4, -6]})

    pd.testing.assert_frame_equal(df_result, df_expected)
