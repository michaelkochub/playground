const { h, app } = hyperapp
/** @jsx h */

/*
 * Basic To Do List with
 * 'Add Item' and 'Clear List'
 * features
 */

app({
  state: {
    items: ["garden", "bathe", "walk"],
    item: "",
  },
  view: (state, actions) => (
    <main>
      <b>To Do</b>
      <ul>
        {state.items.map(item => <li>{item}</li>)}
      </ul>
      <input 
        type="text"
        placeholder="add to do item here..."
        onblur={e => actions.setItem(e.target.value)}
        value="" />
      <button onclick={actions.addItem}>Add Item</button>
      <button onclick={actions.clearList}>Clear</button>
    </main>
  ),
  actions: {
    addItem: state => ({ 
      items: [...state.items, state.item],
      item: "",
    }),
    clearList: state => ({ items: [] }),
    setItem: (state, actions, value) => ({ item: value }),
  }
})
