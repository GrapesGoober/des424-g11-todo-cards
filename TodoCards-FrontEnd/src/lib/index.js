// place files you want to import through the `$lib` alias in this folder.
const ENDPOINT = "/api"

// route to the login page upon unsuccessful login
const LOGIN_HREF = "/login"

async function sendBackendRequest(route, body) {
    let response = await fetch(ENDPOINT + route, {
        method: "POST",
        credentials: "include",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(body)
    })

    return await response.json()
}

async function sendAuthBackendRequest(route, body) {
    let result = await sendBackendRequest(route, body)
    if (result === false) {
        await logout()
        window.location.href = LOGIN_HREF
    }
    return result
}

let ping_count = 0
export async function ping() {

    let result = await sendBackendRequest("/ping", {})
    if (result.message === "pong"){
        ping_count ++
    }

    return ping_count
}

export async function login(username, password){
    return await sendBackendRequest("/login", {username, password})
}

export async function signup(username, password){
    return await sendBackendRequest("/signup", {username, password})
}

export async function logout() {
    await sendBackendRequest("/logout", {})
    return false
}

export async function getDeckslist(){
    return await sendAuthBackendRequest("/get-decks-list", {})
}

export async function getCardslist(deckId){
    return await sendAuthBackendRequest("/get-cards-list", {deckId})
}

export async function getSubcardslist(cardId){
    return await sendAuthBackendRequest("/get-subcards-list", {cardId})
}

export async function editCard(cardInfo){
    return await sendAuthBackendRequest("/edit-card", {cardInfo})
}

export async function editSubcard(subcardInfo){
    return await sendAuthBackendRequest("/edit-subcard", {subcardInfo})
}

export async function editDeck(deckInfo){
    return await sendAuthBackendRequest("/edit-deck", {deckInfo})
}

export async function createCard(deckId, cardInfo){
    return await sendAuthBackendRequest("/create-card", {deckId, cardInfo})
}

export async function createSubcard(cardId, subcardInfo){
    return await sendAuthBackendRequest("/create-subcard", {cardId, subcardInfo})
}

export async function createDeck(deckInfo){
    return await sendAuthBackendRequest("/create-deck", {deckInfo})
}

export async function deleteCard(cardId){
    return await sendAuthBackendRequest("/delete-card", {cardId})
}

export async function deleteSubcard(subcardId){
    return await sendAuthBackendRequest("/delete-subcard", {subcardId})
}

export async function deleteDeck(deckId){
    return await sendAuthBackendRequest("/delete-deck", {deckId})
}

export async function finishCard(cardId, isUnfinished){
    return await sendAuthBackendRequest("/finish-card", {cardId, isUnfinished})
}
export async function finishSubcard(subcardId, isUnfinished){
    return await sendAuthBackendRequest("/finish-subcard", {subcardId, isUnfinished})
}

export async function getSharecode(deckId, accessType){
    return await sendAuthBackendRequest("/get-sharecode", {deckId, accessType})
}

export async function recieveSharecode(sharecode){
    return await sendAuthBackendRequest("/recieve-sharecode", {sharecode})
}

export async function getAccessList(deckId){
    return await sendAuthBackendRequest("/get-access-list", {deckId})
}

export async function removeAccess(deckId, username) {
    return await sendAuthBackendRequest("/remove-access", {deckId, username})
}


export async function adminGetEverything() {
    return await sendAuthBackendRequest("/get-everything", {})
}

export async function adminDeleteUser(username) {
    return await sendAuthBackendRequest("/delete-user", {username})
}