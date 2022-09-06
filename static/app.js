const log_in= Vue.component('LogIn',{
    template:`
    <div>
        <form method="Post" style="margin:0 auto;width:75%;text-align:left">
            <div class="form-group">
              <label>Username</label>
              <input type="text" class="form-control" id="name" placeholder="Enter username" name="user_name">
            </div>
            <div class="form-group">
              <label>Password</label>
              <input type="password" class="form-control" id="password" placeholder="Password" name="password">
            </div>
            <div class="form-group">
              <label>E-Mail</label>
              <input type="text" class="form-control" id="email" placeholder="E-Mail" name="email">
            </div>
            <button type="submit" class="btn btn-primary" name="Go" value="Sign Up">Sign Up</button>
            <button type="submit" class="btn btn-primary" name="Go" value="Log In">Log In</button>
        </form>
    </div>
    `
}
)
const dashboard= Vue.component('dashboard',{
    template:`
    <form method="Post" style="margin:0 auto;width:50%;text-align:left">
      <button type="submit" class="btn btn-outline-dark" name="Go" value="add_deck">Add Deck</button>
      <button type="submit" class="btn btn-outline-dark" name="Go" value="view_decks">View Decks</button>
    </form>
    `
})
const deck_form= Vue.component('deck_form',{
    template:`
    <form method="Post" style="margin:0 auto;width:70%;text-align:left">
        <div class="form-group">
          <label>Deck Name</label>
          <input type="text" class="form-control" placeholder="Enter deck name" name="deck_name">
        </div>
        <button type="submit" class="btn btn-outline-dark" >Add Deck</button>
    </form>
    `
})

const edit_deck= Vue.component('edit_deck',{
    template:`
    <form method="Post" style="margin:0 auto;width:70%;text-align:left">
        <div class="form-group">
          <label>Deck Name</label>
          <input type="text" class="form-control" placeholder="Enter deck name to delete deck" name="deck_name">
        </div>
        <button type="submit" class="btn btn-outline-dark" name="Go" value="delete_deck">Delete deck</button>
        <p style="color:red">{{ warning_delete }}</p>
        <h1>Add Card</h1>
        <div class="form-group">
            <label>Deck Name</label>
            <input type="text" class="form-control" placeholder="Enter deck name" name="deck">
        </div>
        <p style="color:red">{{ warning_deck }}</p>
        <div class="form-group">
            <label>Question</label>
            <input type="text" class="form-control" placeholder="Enter Question" name="ques">
        </div>
        <p style="color:red">{{ warning_card }}</p>
        <div class="form-group">
            <label>Answer</label>
            <input type="text" class="form-control" placeholder="Enter Answer" name="ans">
        </div>
        <button type="submit" class="btn btn-outline-dark" name="Go" value="add_card">Add card</button>
        <button type="submit" class="btn btn-outline-dark" name="Go" value="delete_card">Delete card</button>
        <p style="color:red">{{ warning }}</p>
        <button type="submit" class="btn btn-outline-dark" name="Go" value="back">Back</button>
    </form>
    `
})

const view_card= Vue.component('view_card',{
    template:`
    <form method="Post" style="margin:0 auto;width:70%;text-align:left">
        <div class="form-group">
          <label>Deck Name</label>
          <input type="text" class="form-control" placeholder="Enter deck name" name="deck_name">
        </div>
        <p style="color:red">{{ warning }}</p>
        <button type="submit" class="btn btn-outline-dark" name="Go" value="view">View</button>
        <button type="submit" class="btn btn-outline-dark" name="Go" value="back">Back</button>
        <button type="submit" class="btn btn-outline-dark" name="Go" value="export_cards">Export Cards</button>
    </form>
    `
})

const update_deck= Vue.component('update_deck',{
    template:`
    <form method="Post" style="margin:0 auto;width:70%;text-align:left">
        <div class="form-group">
          <label>Old deck Name</label>
          <input type="text" class="form-control" placeholder="Enter deck name" name="old_name">
        </div>
        <div class="form-group">
            <label>New deck Name</label>
            <input type="text" class="form-control" placeholder="Enter new deck name" name="new_name">
        </div>
        <button type="submit" class="btn btn-outline-dark" name="Go" value="back">Back</button>
    </form>
    `
})
const routes=[{
    path: '/',
    component: log_in
}
]
const router = new VueRouter({
    routes
})
var app=new Vue({
    el:"#app",
    router: router
})