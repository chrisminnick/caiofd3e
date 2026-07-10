import Message from './bk07ch05_listing18.jsx';
function ErrorMessage(props) {
  return <Message messageType="error" messageText={props.errorMessage} />;
}
export default ErrorMessage;
