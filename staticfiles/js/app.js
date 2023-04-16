const dropdown = () => {
    nav = document.querySelector(`nav`)
    nav.classList.toggle(`open`)
}

const drop = (clas) => {
    nav = document.querySelector(`.${clas}`)
    nav.classList.toggle(`down`)
}

const dropSubject = (clas) => {
    nav = document.querySelector(`.${clas}`)
    nav.classList.toggle(`create_subject_down`)
}

const drop_to_zero = (clas) => {
    nav = document.querySelector(`.${clas}`)
    nav.classList.toggle(`down_zero`)
}

const dropAll = (arr) => {
    for (const element of arr) {
        drop(element)
    }
}

const appier = (clas) => {
    nav = document.querySelectorAll(`.${clas}`)
    nav.forEach(element => {
        element.classList.toggle(`hide`)
    });
}

const editNote = () => {
    const content = document.querySelector('.note_content')
    const text = content.textContent
    const formattedText = text.replaceAll('\n', '<br>').replaceAll('<title>', '<h1>').replaceAll('</title>', '</h1>').replaceAll('<hr>', '<hr class="p_hr">')
    content.innerHTML = formattedText
}

try {
    editNote()
}
catch {

}

const editAnswer = () => {
    document.querySelectorAll('.edit_answer').forEach(content => {
        const text = content.textContent
        const formattedText = text.replaceAll('<next>', '&').replaceAll('<include>', '; must include: <b>').replaceAll('</include>', '</b>')
        content.innerHTML = formattedText
    })
}

try {
    editAnswer()
}
catch {

}

const editP = () => {
    const content = document.querySelector('.editP')
    const text = content.textContent
    const formattedText = text.replaceAll('\n', ' ').replaceAll('<title>', '').replaceAll('</title>', '').replaceAll('<hr>', '')
    content.textContent = formattedText
}

try {
    editP()
}
catch {

}

try {
    document.querySelectorAll(`.test_input_check`).forEach(x => {
        x.addEventListener('click', (e) => {
            e.preventDefault()
        })
    })
}

catch {

}

const testFinish = (index, q_options, answer_correct) => {
    q_options = q_options.map(x => {
        return x == "True" ? true : false;
    })

    const [case_s, dia_s, sym_s, mashed] = q_options

    index--
    const question = document.querySelectorAll(`.test_card`)[index]
    let answer = document.querySelectorAll('.test_input')[index].value

    const get_answers = (str) => {
        const new_str = str.replaceAll('</include>', '')
        let inclu = [new_str.split('<include>')[1]]
        let ans = new_str.split('<include>')[0].split('<next>')

        if (inclu == undefined && ans == undefined){
            ans = [str]
        }

        ans = ans.map(x => {return x.trim()})
        inclu = inclu.map(x => {
            if (x) {
                return x.trim()
            }
        })

        return [ans, inclu[0] ? inclu : ['']]
    }

    let [answers, must_include] = get_answers(answer_correct)

    if (!case_s) {
        answers = answers.map(str => {return str.toLowerCase()})
        must_include = must_include.map(str => {return str.toLowerCase()})
        answer = answer.toLowerCase()

    }
    if (!dia_s) {
        answers = answers.map(str => {return str.normalize("NFD").replace(/[\u0300-\u036f]/g, "")})
        must_include = must_include.map(str => {return str.normalize("NFD").replace(/[\u0300-\u036f]/g, "")})
        answer = answer.normalize("NFD").replace(/[\u0300-\u036f]/g, "")

    }
    if (!sym_s) {
        answers = answers.map(str => {return str.replace(/[^a-zA-Z0-9, ]/g, '')})
        must_include = must_include.map(str => {return str.replace(/[^a-zA-Z0-9, ]/g, '')})
        answer = answer.replace(/[^a-zA-Z0-9, ]/g, '')
    }
    
    if (mashed) {
        let option1 = []
        let option2 = []
        let option3 = []
        let option4 = []
        let option5 = []
        let option6 = []

        if (answer != ''){
            option1 = answers.map(str => str.replaceAll(answer, '').trim())
            option2 = answers.map(str => str.replaceAll(answer.replaceAll(',', '').trim(), '').trim())
            option3 = answers.map(str => str.trim().replaceAll(',', '').replaceAll(answer, '').trim())
            option4 = answers.map(str => str.trim().replaceAll(',', '').replaceAll(answer.replaceAll(',', '').trim(), '').trim())
            option5 = answers.map(str => str.trim().replaceAll(answer, '').trim())
            option6 = answers.map(str => str.trim().replaceAll(answer.replaceAll(',', '').trim(), '').trim())
        }

        if (option1 == '') {
            if (!answers.includes(answer)){
                answers.push(answer)
            }
        }
        if (option2 == '') {
            if (!answers.includes(answer)){
                answers.push(answer)
            }
        }
        if (option3 == '') {
            if (!answers.includes(answer)){
                answers.push(answer)
            }
        }
        if (option4 == '') {
            if (!answers.includes(answer)){
                answers.push(answer)
            }
        }
        if (option5 == '') {
            if (!answers.includes(answer)){
                answers.push(answer)
            }
        }
        if (option6 == '') {
            if (!answers.includes(answer)){
                answers.push(answer)
            }
        }
    }

    const message = document.querySelectorAll(`.correct_message`)[index]
    const ans = document.querySelectorAll(`.correct_answer`)[index]

    const compare = (str, arr) => {
        for (const ele of arr) {
            str = str.replace(`${ele}`, '')
            str = str.replace(`${must_include}`, '')
        }
    
        str = str.replace(/[^a-zA-Z0-9 ]/g, '')

        console.log(str)

        return str.trim().length > 0 ? false : true
    }

    const correctAnswer = () => {
        message.textContent = 'Correct'
        ans.textContent = answer

        message.classList.add('correct')
        ans.classList.add('correct')
    }

    const incorrectAnswer = () => {
        message.textContent = 'Wrong'
        ans.textContent = answer

        message.classList.add('wrong')
        ans.classList.add('wrong')
    }

    if (must_include != "") {
        console.log(compare(answer, answers));
        console.log(answer.includes(must_include));
        if (compare(answer, answers) && answer.includes(must_include)) {
            correctAnswer()
        } else if (answers.includes('') && answer.includes(must_include) && answers.includes(answer) && answers.length == 2) {
            correctAnswer()
        } else {
            incorrectAnswer()
        }
    } else if (compare(answer, answers)) {
        correctAnswer()
    } else {
        incorrectAnswer()
    }
}

const testComplete = () => {
    document.querySelectorAll(`.test_card`).forEach(x => {
        x.classList.add('test_card_active')
    })
}

const openTestQuestion = (index, q_options, answer_correct) => {
    q_options = q_options.map(x => {
        return x == "True" ? true : false;
    })

    const [case_s, dia_s, sym_s, mashed] = q_options

    index--
    const question = document.querySelectorAll(`.test_card`)[index]
    let answer = document.querySelectorAll('.test_input')[index].value

    const get_answers = (str) => {
        const new_str = str.replaceAll('</include>', '')
        let inclu = [new_str.split('<include>')[1]]
        let ans = new_str.split('<include>')[0].split('<next>')

        if (inclu == undefined && ans == undefined){
            ans = [str]
        }

        ans = ans.map(x => {return x.trim()})
        inclu = inclu.map(x => {
            if (x) {
                return x.trim()
            }
        })

        return [ans, inclu[0] ? inclu : ['']]
    }

    let [answers, must_include] = get_answers(answer_correct)

    if (!case_s) {
        answers = answers.map(str => {return str.toLowerCase()})
        must_include = must_include.map(str => {return str.toLowerCase()})
        answer = answer.toLowerCase()

    }
    if (!dia_s) {
        answers = answers.map(str => {return str.normalize("NFD").replace(/[\u0300-\u036f]/g, "")})
        must_include = must_include.map(str => {return str.normalize("NFD").replace(/[\u0300-\u036f]/g, "")})
        answer = answer.normalize("NFD").replace(/[\u0300-\u036f]/g, "")

    }
    if (!sym_s) {
        answers = answers.map(str => {return str.replace(/[^a-zA-Z0-9, ]/g, '')})
        must_include = must_include.map(str => {return str.replace(/[^a-zA-Z0-9, ]/g, '')})
        answer = answer.replace(/[^a-zA-Z0-9, ]/g, '')
    }
    
    if (mashed) {
        let option1 = []
        let option2 = []
        let option3 = []
        let option4 = []
        let option5 = []
        let option6 = []

        if (answer != ''){
            option1 = answers.map(str => str.replaceAll(answer, '').trim())
            option2 = answers.map(str => str.replaceAll(answer.replaceAll(',', '').trim(), '').trim())
            option3 = answers.map(str => str.trim().replaceAll(',', '').replaceAll(answer, '').trim())
            option4 = answers.map(str => str.trim().replaceAll(',', '').replaceAll(answer.replaceAll(',', '').trim(), '').trim())
            option5 = answers.map(str => str.trim().replaceAll(answer, '').trim())
            option6 = answers.map(str => str.trim().replaceAll(answer.replaceAll(',', '').trim(), '').trim())
        }

        if (option1 == '') {
            if (!answers.includes(answer)){
                answers.push(answer)
            }
        }
        if (option2 == '') {
            if (!answers.includes(answer)){
                answers.push(answer)
            }
        }
        if (option3 == '') {
            if (!answers.includes(answer)){
                answers.push(answer)
            }
        }
        if (option4 == '') {
            if (!answers.includes(answer)){
                answers.push(answer)
            }
        }
        if (option5 == '') {
            if (!answers.includes(answer)){
                answers.push(answer)
            }
        }
        if (option6 == '') {
            if (!answers.includes(answer)){
                answers.push(answer)
            }
        }
    }

    const message = document.querySelectorAll(`.correct_message`)[index]
    const ans = document.querySelectorAll(`.correct_answer`)[index]

    const compare = (str, arr) => {
        for (const ele of arr) {
            str = str.replace(`${ele}`, '')
            str = str.replace(`${must_include}`, '')
        }
    
        str = str.replace(/[^a-zA-Z0-9 ]/g, '')

        console.log(str)

        return str.trim().length > 0 ? false : true
    }

    const correctAnswer = () => {
        message.textContent = 'Correct'
        ans.textContent = answer

        message.classList.add('correct')
        ans.classList.add('correct')
    }

    const incorrectAnswer = () => {
        message.textContent = 'Wrong'
        ans.textContent = answer

        message.classList.add('wrong')
        ans.classList.add('wrong')
    }

    if (must_include != "") {
        console.log(compare(answer, answers));
        console.log(answer.includes(must_include));
        if (compare(answer, answers) && answer.includes(must_include)) {
            correctAnswer()
        } else if (answers.includes('') && answer.includes(must_include) && answers.includes(answer) && answers.length == 2) {
            correctAnswer()
        } else {
            incorrectAnswer()
        }
    } else if (compare(answer, answers)) {
        correctAnswer()
    } else {
        incorrectAnswer()
    }

    question.classList.add('test_card_active')
}