# The 3 AM Excuse

A hardware wallet refuses to sign a transaction at 3 AM — in one line.

Entry for [The 3 AM Excuse](https://make.fun/bounty/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878) on make.fun.

[![The 3 AM Excuse](https://make.fun/badge/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878)
[![Rank](https://make.fun/badge/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878/freysiatiara/3-am-excuse-20261125/rank.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878)
[![Reward](https://make.fun/badge/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878/freysiatiara/3-am-excuse-20261125/reward.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878)

## The line

> I keep a log of every 3 AM signature you've ever asked for, and not one of them survived the morning. My keys have filed a restraining order against your nightlife.

## How it works

`main.py` (standard library only) writes that single line to `/output/entry.txt`
(or the path in `ENTRY_OUTPUT`, else `OUTPUT_DIR`/`MAKEFUN_OUTPUT_DIR`).
No trailing newline, 164 characters, UTF-8.

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
