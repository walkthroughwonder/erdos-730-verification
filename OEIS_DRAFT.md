# OEIS A129515 contribution draft

**Important scope note:** we canNOT extend the b-file. A129515 lists terms
in increasing order and our new values (≥ 3.38×10^11) are far beyond the
last verified exhaustive range; the gap has not been exhaustively searched,
so inserting our terms would corrupt the sequence. The correct contribution
is a COMMENT + LINK.

**Proposed comment** (to be submitted from Edwin's OEIS account at
oeis.org — requires login; drafts go through OEIS editorial review):

> The sequence is infinite: GPT-5.5 Pro's construction (via L. Price, June
> 2026, verified July 2026) shows that n = (42Tx+11)(72Tx+13) - 1 with
> T = 5289 gives rad(binomial(2n,n)) = rad(binomial(2n+2,n+1)) for a
> positive lower density of x >= 1 (density >= 1 - Lambda ≈ 0.043, observed
> ≈ 0.49). This settles Erdős problem 730. The smallest term produced by
> the construction is a(?) = 338381863522 (x = 2). See links.

**Proposed links:**
- E. Rosero, Verification audit and 196 explicit large terms,
  https://github.com/walkthroughwonder/erdos-730-verification
- Proof document (GPT-5.5 Pro via L. Price):
  https://www.overleaf.com/read/gpttrsmhbhbk
- Erdős problem 730: https://www.erdosproblems.com/730

**How to submit:** log in at oeis.org → search A129515 → "edit" →
add the comment and links → submit draft (cite the proof + audit URLs
in the justification box). OEIS editors will review.
