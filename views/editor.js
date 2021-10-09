import * as React from "https://esm.sh/react";
import * as ReactDOM from "https://esm.sh/react-dom";
import CodeMirror from 'https://esm.sh/@uiw/react-codemirror@4.0.1';
import { StreamLanguage } from 'https://esm.sh/@codemirror/stream-parser';
import { python } from 'https://esm.sh/@codemirror/lang-python';

export function bind(node, config) {
  return {
    create: (component, props, children) =>
      React.createElement(component, props, ...children),
    render: (element) => ReactDOM.render(element, node),
    unmount: () => ReactDOM.unmountComponentAtNode(node),
  };
}

export function Editor({ onChange }) {
  return React.createElement(
    CodeMirror,
    {
      placeholder: "...",
      theme: "light",
      minWidth: "900px",
      style: {"border": "1px solid #cccccc"},
      onChange: (value) => onChange(value),
    }
  );
}
