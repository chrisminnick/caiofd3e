const pet = { name: "Murray", type: "domestic short hair" };
for (const property in pet) {
  console.log(`${property}: ${pet[property]}`);
}
