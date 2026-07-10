function CustomerList({ customers }) {
  return (
    <ul>
      {customers.map((customer) => (
        <li key={customer.customerId}>
          {customer.address}, {customer.city},{customer.state}
        </li>
      ))}
    </ul>
  );
}
export default CustomerList;
