"""Custom exceptions for the Mother-of-AI application."""


class RepositoryException(Exception):
    """Base exception for repository-related errors."""


class PaperNotFound(RepositoryException):
    """Exception raised when paper data is not found."""


class PaperNotSaved(RepositoryException):
    """Exception raised when paper data is not saved."""


class ParsingException(Exception):
    """Base exception for parsing-related errors."""


# Week 2+: PDF parsing exceptions (not implemented in Week 1)
# class PDFParsingException(ParsingException):
#     """Base exception for PDF parsing-related errors."""


# Week 3+: OpenSearch exceptions (placeholders for Week 1)
class OpenSearchException(Exception):
    """Base exception for OpenSearch-related errors."""


# Week 6+: LLM exceptions (placeholders for Week 1)
class LLMException(Exception):
    """Base exception for LLM-related errors."""


# General application exceptions
class ConfigurationError(Exception):
    """Exception raised when configuration is invalid."""
