What Is the SageMaker JumpStart Industry Python SDK
===================================================

The SageMaker JumpStart Industry Python SDK is an open source client library for
processing text datasets, training ML language models such as BERT and its variants,
and deploying industry-focused
machine learning models on `Amazon SageMaker JumpStart
<https://docs.aws.amazon.com/sagemaker/latest/dg/studio-jumpstart-industry.html>`_.

.. include:: ../../README.rst
   :start-after: inclusion-marker-1-1-starting-do-not-remove
   :end-before:  inclusion-marker-1-1-ending-do-not-remove


How It Works
------------

The following architecture diagram shows what the ``smjsindustry`` library covers
in the ML lifecycle.

.. image:: images/smjsindustry_system.png
   :alt: An architecture diagram of SageMaker JumpStart end-to-end solutions
       and the coverage of SageMaker JumpStart Industry Python SDK

#. Use SageMaker JumpStart Industry notebooks for solutions, models, and examples.
   The notebooks include sections of using the ``smjsindustry`` library to process
   industry text data. To find the notebooks on SageMaker JumpStart, see [Add link].
   To find a preview of the example notebooks in finance, see the
   [Add link].
#. The SageMaker JumpStart Industry Python SDK helps run SageMaker
   processing jobs to process input text data into a multimodal dataset.
   You can encrypt the Amazon S3 bucket and processing containers using Amazon VPC.
#. After the processing job has completed, SageMaker copies the result from
   the processing containers to the Amazon S3 bucket.
   SageMaker terminates the processing job and its resources.
#. You can download the result from the Amazon S3 bucket to the Studio notebook kernel
   and you can start training pretrained language models,
   such as BERT and its variants.
#. You evaluate the model performance and start using the model for making prediction.


What It Does
------------

The library provides API operations to process financial multimodal
(tabular and long-form text) datasets for machine learning.
It provides a set of finance text analysis capabilities as follows:

- It retrieves SEC Filings from the SEC EDGAR database.
- It calculates NLP scores for text data of the SEC Filings.
- It summarizes text data using the :class:`~smjsindustry.Summarizer` class,
  choosing between the Jaccard and k-medoids algorithms.
- It combines text data, tabular data, and categorical data into a multimodal dataset.
- It provides pretrained RoBERTa-SEC language models with
  S&P 500 10-K/Q filings over the last decades and the English wikipedia corpus.


What It Offers
--------------

The SageMaker JumpStart Industry Python SDK is a client library
of SageMaker JumpStart.
The SageMaker JumpStart Industry materials consist of the following:

- The SageMaker JumpStart Industry Python SDK
- `3 JumpStart finance example notebooks on SageMaker Studio <https://docs.aws.amazon.com/sagemaker/latest/dg/studio-jumpstart-industry.html#studio-jumpstart-industry-examples>`_

  - SEC filing retrieval, NLP scoring and summarization
  - Paycheck protection program loan return classification
  - SEC standard industry code (SIC) multi-class classification

  To see an overview of the notebooks, see `Tutorials in Finance <notebooks/index.html>`_.

- `4 RoBERTa-SEC text embedding model cards in the JumpStart model zoo <https://docs.aws.amazon.com/sagemaker/latest/dg/studio-jumpstart-industry.html#studio-jumpstart-industry-models>`_
- `1 JumpStart solution for corporate credit rating solution <https://docs.aws.amazon.com/sagemaker/latest/dg/studio-jumpstart-industry.html#studio-jumpstart-industry-solutions>`_
