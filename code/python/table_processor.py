'''

'''
import state_transition
import pandas as pd

test = ((1, "f", "new", "new"),
        (2, "f", "trade", "pfilled"),
        (3, "f", "cancel", "canceled"),
        (1, "s", "new", "new"),
        (2, "s", "trade", "filled"),
        (1, "s1", "new", "new"),
        (2, "s1", "amend", "new"),
        (3, "s1", "cancel", "canceled"))

df = pd.DataFrame(test, columns=["seq", "ord", "trans", "state"])

st = state_transition.StateTransitionDiagram(df, "seq", "ord", "trans", "state")
st.draw_state_transitions_diagram()


