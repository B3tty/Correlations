# Correlations

According to [this document](https://ai.stanford.edu/~ronnyk/2009controlledExperimentsOnTheWebSurvey.pdf), a good randomization algorithm for ab tests must have the following properties:

1. End users must be equally likely to see each variant of an experiment (assuming a 50–50 split). There should be no bias toward any particular variant.
2. Repeat assignments of a single end user must be consistent; the end user should be assigned to the same variant on each successive visit to the site.
3. When multiple experiments are run, there must be no correlation between experiments. An end user’s assignment to a variant in one experiment must have no effect on the probability of being assigned to a variant in any other experiment.

Randomization algorithms may optionally support the following two desirable properties:

4. The algorithm may support monotonic ramp-up, meaning that the percentage of users who see a Treatment can be slowly increased without changing the assignments of users who were previously assigned to that Treatment. Supporting this property allows the Treatment percentage to be slowly increased without impairing the user experience or damaging the validity of the experiment.
5. The algorithm may support external control, meaning that users can be manually forced into and out of variants. This property makes it easier to test the experimental site.

This project's goal is to check correlations for ab-testing repartition with a few hashing methods. We are going to check mainly properties 1 and 3 for a few possible repartition functions.

_"We tested this technique using several popular hash functions and a methodology similar to the one we used on the pseudorandom number generators. While any hash function will satisfy the second requirement (by definition), satisfying the first and third is more difficult. We tested five simulated experiments against one million sequential user IDs. We ran chi-square tests to look for violations of the first and third requirements of a randomization algorithm and found that only the cryptographic hash function MD5 generated no correlations between experiments. SHA256 (another cryptographic hash) came close, requiring a five-way interaction to produce a correlation. Other hash functions (including the string hashing algorithm built into .net) failed to pass even a two-way interaction test."_
