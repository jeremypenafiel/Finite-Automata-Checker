import React from "react";
import Form from "react-bootstrap/Form";
import InputGroup from "react-bootstrap/InputGroup";

interface TransitionFunctionTemplateFormProps {
  ruleNumber: number;
  currentState: string;
  inputSymbol: string;
  stackTop: string;
  nextState: string;
  stackPush: string;
}

const TransitionFunctionTemplateForm: React.FC<
  TransitionFunctionTemplateFormProps
> = ({
  ruleNumber,
  currentState,
  inputSymbol,
  stackTop,
  nextState,
  stackPush,
}) => {
  return (
    <InputGroup>
      <InputGroup.Text>Rule: {ruleNumber + 1} </InputGroup.Text>
      <Form.Control
        readOnly
        value={currentState}
        placeholder={currentState}
        name={`CurrentState ${ruleNumber}`}
      />

      <Form.Control
        readOnly
        value={inputSymbol}
        placeholder={inputSymbol}
        name={`InputSymbol ${ruleNumber}`}
      />
      <Form.Control
        readOnly
        value={stackTop}
        placeholder={stackTop}
        name={`StackTop ${ruleNumber}`}
      />

      <Form.Control
        readOnly
        value={nextState}
        placeholder={nextState}
        name={`NextState ${ruleNumber}`}
      />
      <Form.Control
        readOnly
        value={stackPush}
        placeholder={stackPush}
        name={`StackPush ${ruleNumber}`}
      />
    </InputGroup>
  );
};

export default TransitionFunctionTemplateForm;
