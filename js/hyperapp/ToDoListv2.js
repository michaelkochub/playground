const {h, app} = hyperapp
/** @jsx h */

/*
 * To Do List with additional 'delete item'
 * feature that takes number of list item and
 * removes it from the list 
 */

app({
  state: {
    items: ["garden", "bathe", "cry"],
    item: "",
    deleteIndex: 0,
  },
  view: (state, actions) => (
    <main>
      <ol>
      {state.items.map(item => <li>{item}</li>)}
      </ol>
      <input
        type="text"
        placeholder="Add New Item..."
        onblur={e => actions.setItem(e.target.value)}
        value="" />
      <button onclick={actions.addItem}>Add Item</button>
      <br />
      <input
        type="text"
        placeholder="Delete Item Number..."
        onblur={e => actions.setDelete(e.target.value)}
        value="" />
      <button 
        onclick={actions.deleteItem}
        disabled={state.items.length <= 0}>
        Delete Item
      </button>
      <br />
      <button 
        onclick={actions.clearList}
        disabled={state.items.length <= 0}>
        Clear List
      </button>
    </main>
  ),
  actions: {
    addItem: state => ({ items: [...state.items, state.item] }),
    clearList: state => ({ items: [] }),
    setItem: (state, actions, value) => ({ item: value }),
    setDelete: (state, actions, value) => ({ deleteIndex: value }),
    deleteItem: state => ({ items: state.items.filter((_, i) => i != state.deleteIndex - 1 )}),
  }
})