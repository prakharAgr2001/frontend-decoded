from engine.lib import *
from engine.s3_extra import rows, versus
from engine.s2_extra import trap, verdict
from engine.s4_extra import *

EP = dict(id='S4E19', tag='S4 · E19', short='FORM STATE')


def hook(c):
    title(c, 'SIGN UP', 330, 0.1, 90)
    tt = c.T('type')
    for k in range(10):
        x = 300 + (k % 2) * 480; y = 470 + (k // 2) * 150
        box = (x - 220, y - 45, x + 220, y + 45)
        c.pen.rr(*box, 12, fill=WHITE, outline=INK, w=3)
        c.pen.text(x - 200, y, ['Name', 'Email', 'Phone', 'City', 'Address', 'PIN', 'Password', 'Confirm', 'DOB', 'Referral'][k], 'intm', 26, GREY if not (k == 0 and c.on(tt)) else INK, 'lm')
        if c.on(tt): flash_box(c, box, tt + 0.3 + int((c.t - tt) / 0.5) * 0.5, RED, 0.45)
    tl = c.T('lags')
    if c.on(tl): stamp(c.cv, 540, 1270, 'TYPING LAGS', 80, c.P(tl, 0.35), -4, RED); c.sfx(tl, 'thud')


def two(c):
    title(c, 'TWO WAYS TO HOLD A VALUE', 330, 0.1, 74)
    code(c, 30, 420, 1050, 640, ['// controlled: React holds the value', '<input value={name} onChange={(e) => setName(e.target.value)} />'],
         c.T('Controlled'), 0.15, 22, 'Controlled.jsx', marks=[(1, c.T('every'), YEL)])
    code(c, 30, 700, 1050, 960, ['// uncontrolled: the DOM holds the value', '<input name="name" defaultValue="" />',
                                 "new FormData(form).get('name') // on submit"], c.T('Uncontrolled'), 0.15, 22, 'Uncontrolled.jsx', marks=[(2, c.T('submit'), YEL)])
    te = c.T('every')
    if c.on(te): label(c, 540, 1040, 'controlled: a render on every keystroke', te, (255, 225, 190), INK, 30)


def exam(c):
    title(c, 'THE EXAMINER', 330, 0.1, 110)
    versus(c, ('CONTROLLED', ORANGE, c.T('shoulder'), [(c.T('every'), 'reads over your shoulder'), (c.T('letter'), 'checks every letter')]),
           ('UNCONTROLLED', BLUE, c.T('freely'), [(c.T('freely'), 'you write freely'), (c.T('hand'), 'checked when you hand it in')]), 430, 860, 36)


def more(c):
    title(c, 'MORE THAN VALUES', 330, 0.1, 100, hlcol=YEL)
    items = [('values', 'values', YEL), ('touched', 'touched', (220, 225, 235)), ('dirty', 'dirty', (255, 225, 190)), ('errors', 'errors', (255, 210, 210)),
             ('submitting', 'isSubmitting', (200, 240, 200))]
    for k, (kw, s_, col) in enumerate(items):
        node(c, 540, 480 + k * 140, 560, 100, s_, c.T(kw), fill=col, size=36)
    tl = c.T('library')
    if c.on(tl): label(c, 540, 1230, 'that is why form libraries exist', tl, YEL, INK, 32)


def rhf(c):
    title(c, 'REACT HOOK FORM', 330, c.T('Hook'), 96, hlcol=YEL)
    code(c, 30, 430, 1050, 830, ['const { register, handleSubmit, formState } =', '  useForm({ resolver: zodResolver(schema) });',
                                 "<input {...register('email')} />", '{formState.errors.email?.message}'],
         c.T('Hook') + 0.3, 0.15, 24, 'SignUp.jsx', marks=[(2, c.T('refs'), YEL), (1, c.T('schema'), YEL)])
    rows(c, 90, 920, [(c.T('refs'), 'register: uncontrolled inputs via refs', None, 'ok'), (c.T('subscribe'), 'renders only what you subscribe to', None, 'ok')], 140, 900, 110, 34)


def timing(c):
    title(c, 'WHEN TO SHOW ERRORS', 330, 0.1, 90, hlcol=YEL)
    c.pen.rr(140, 470, 940, 560, 14, fill=WHITE, outline=RED if c.on(c.T('annoying')) else INK, w=4)
    c.pen.text(170, 515, typed_text(c, 'riya@gm', c.T('typing'), 0.15), 'ints', 34, INK, 'lm')
    ta = c.T('annoying')
    if c.on(ta):
        c.pen.text(150, 600, 'Invalid email', 'int', 28, RED, 'lm'); cross(c.pen, 880, 600, 0.6, RED, 6, c.P(ta, 0.3))
    rows(c, 90, 760, [(c.T('submit'), 'first: validate on blur or submit', None, 'ok'), (c.T('fix'), 'then: re-check on every change', 'so the error clears as they fix it', 'ok')],
         170, 900, 140, 34, 26)
    tr = c.T('Reward')
    if c.on(tr): label(c, 540, 1150, 'reward early, punish late', tr, YEL, INK, 36)


def actions(c):
    title(c, 'REACT 19 FORM ACTIONS', 330, 0.1, 84, hlcol=YEL)
    code(c, 30, 430, 1050, 760, ['const [state, formAction, pending] =', '  useActionState(signUp, null);', '<form action={formAction}>',
                                 '  <button disabled={pending}>Sign up</button>'], c.T('action'), 0.15, 26, 'SignUp.jsx', marks=[(2, c.T('pending'), YEL)])
    chapter(c, 540, 870, 'S2 · E15', 'Server Actions', c.T('season'))
    tw = c.T('works')
    if c.on(tw): label(c, 540, 990, 'with a server action, the form works before JS loads', tw, WHITE, INK, 28)


def gotcha(c):
    trap(c, 'Interview')
    txt(c, 540, 460, 'Why does my input lose focus on every keystroke?', c.T('focus'), 'intx', 40, INK)
    code(c, 30, 540, 1050, 820, ['function Form() {', '  const Field = () => <input ... />; // new type!', '  return <Field />;', '}'],
         c.T('inside'), 0.15, 26, 'bug.jsx', marks=[(1, c.T('identity'), YEL)])
    tr = c.T('remounts')
    if c.on(tr): label(c, 540, 900, 'new component type → unmount + remount → focus lost', tr, (255, 210, 210), INK, 28)
    to = c.T('outside')
    if c.on(to): label(c, 540, 1000, 'define components outside · keep keys stable', to, (200, 240, 200), INK, 30)


SCENES = [
    (hook, "A sign up form with twenty fields. You type one letter in the name field, and every field re-renders. On a cheap phone, typing lags."),
    (two, "There are two ways to hold an input's value. Controlled: React state holds it, and every keystroke calls set state, which means a render. Uncontrolled: the DOM holds it, and you read it on submit."),
    (exam, "Controlled is an examiner reading over your shoulder, checking every letter. Uncontrolled: you write freely, and it's checked when you hand it in."),
    (more, "And form state is more than values. Which fields were touched. Which are dirty, meaning changed. The errors. And whether it's submitting. That's why every serious app uses a form library."),
    (rhf, "React Hook Form is the popular one. Register wires inputs through refs, so they stay uncontrolled. Validation comes from a schema. And components only re-render for the state they subscribe to."),
    (timing, "Timing matters too. Showing an error while someone is still typing their email is annoying. So validate on blur, or on submit first. After that, re-check on every change, so the error clears the moment they fix it. Reward early, punish late."),
    (actions, "React nineteen adds form actions. Use action state gives you the result and a pending flag. Remember server actions from season two? With one, the form even works before JavaScript loads."),
    (gotcha, "Interview trap: why does my input lose focus on every keystroke? Because a component was defined inside another component. Every render creates a new identity, so React unmounts and remounts the input. Define components outside, and keep keys stable."),
    (scene_next('S4 · E20', 'STATE MACHINES', 'make impossible states impossible', 'machines', 'impossible'),
     "Next: state machines, and how to make impossible states impossible. Comment NOTES for the cheat sheet."),
]
