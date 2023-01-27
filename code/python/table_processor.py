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

states_list = ["state"]
trans_list = ["trans"]
obj_list = ["ord"]
seq_list = ["seq"]

st = state_transition.StateTransitionDiagram(df, seq_list, obj_list, trans_list, states_list)
st.draw_state_transitions_diagram()


