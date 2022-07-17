const rewire = require("rewire")
const app = rewire("../app")
const openNav = app.__get__("openNav")
// @ponicode
describe("openNav", () => {
    test("0", () => {
        document.body.insertAdjacentHTML("afterbegin", `<div id="wrapper0"><div>
        	<div id="mySidenav"></div>
        </div>
        </div>`)
        let result = openNav()
        expect(result).toMatchSnapshot()
        expect(document.getElementById("wrapper0")).to.matchSnapshot()
        document.body.removeChild(document.getElementById("wrapper0"))
    })
})
