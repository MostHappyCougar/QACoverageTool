'''

'''
import state_transition
import pandas as pd

test = ((1, "f", "new", "new", "a"),
        (2, "f", "trade", "pfilled", "s"),
        (3, "f", "cancel", "canceled", "d"),
        (1, "s", "new", "new", "f"),
        (2, "s", "trade", "filled", "f"),
        (1, "s1", "new", "new", "r"),
        (2, "s1", "amend", "new", "d"),
        (3, "s1", "cancel", "canceled", "a"))

df = pd.DataFrame(test, columns=["seq", "ord", "trans", "state", "test"])

list_of_state = ["state"]

st = state_transition.StateTransitionDiagram(df, ["seq"], ["ord"], ["trans"], list_of_state)
st.draw_state_transitions_diagram()


