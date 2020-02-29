import * as React from "react";
import { render } from "react-dom";

import App from "./App";
import eel from "./eel";

eel.helloFriendsPY("JS");

render(<App />, document.getElementById("root"));
